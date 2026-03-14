"""
convert.py — Converte Casa_do_Mosteiro_v6.xlsx → reservas.json
Executado automaticamente pelo GitHub Actions a cada push do Excel.
"""
import json, glob, sys
from openpyxl import load_workbook

# Encontra o ficheiro Excel (aceita qualquer nome *.xlsx)
files = glob.glob('*.xlsx')
if not files:
    print("❌ Nenhum ficheiro .xlsx encontrado")
    sys.exit(1)

xlsx = sorted(files)[-1]   # usa o mais recente se houver vários
print(f"📂 A processar: {xlsx}")

wb = load_workbook(xlsx, data_only=True)

# Tenta encontrar a folha de reservas
sheet_name = None
for name in wb.sheetnames:
    if 'serva' in name.lower() or 'eserv' in name.lower():
        sheet_name = name
        break
if not sheet_name:
    sheet_name = wb.sheetnames[0]

ws = wb[sheet_name]
print(f"📋 Folha: {sheet_name}")

# Encontra linha de cabeçalho
header_row = None
for r in range(1, 6):
    row_vals = [str(ws.cell(r, c).value or '').strip() for c in range(1, 17)]
    if 'Voyageur' in row_vals or 'Voyageur' in ' '.join(row_vals):
        header_row = r
        break

if not header_row:
    print("❌ Cabeçalho não encontrado")
    sys.exit(1)

# Mapeamento de colunas
hdr = [str(ws.cell(header_row, c).value or '').strip() for c in range(1, 17)]
def col(key):
    for i, h in enumerate(hdr):
        if key.lower() in h.lower():
            return i + 1
    return None

iPlat  = col('Plateforme') or col('Plataforma')
iName  = col('Voyageur')   or col('Nome')
iIn    = col('Arriv')      or col('Chegada') or col('Entrada')
iOut   = col('D\u00e9part') or col('D\xe9part') or col('Sa\xedda') or col('Saida')
iG     = col('Personnes')  or col('Pessoas')
iHour  = col('Hora')       or col('Heure')
iPhone = col('T\xe9l\xe9') or col('Telef') or col('Phone')

print(f"Colunas: plat={iPlat} name={iName} in={iIn} out={iOut} guests={iG} hour={iHour} phone={iPhone}")

def to_ymd(v):
    if v is None: return None
    from datetime import datetime, date
    if isinstance(v, (datetime, date)):
        return v.strftime('%Y-%m-%d')
    s = str(v).strip()
    import re
    m = re.match(r'^(\d{2})/(\d{2})/(\d{4})', s)
    if m: return f"{m[3]}-{m[2]}-{m[1]}"
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', s)
    if m: return s[:10]
    return None

reservations = []
for r in range(header_row + 1, ws.max_row + 1):
    name = ws.cell(r, iName).value  if iName  else None
    plat = ws.cell(r, iPlat).value  if iPlat  else None
    ci   = to_ymd(ws.cell(r, iIn).value)  if iIn   else None
    co   = to_ymd(ws.cell(r, iOut).value) if iOut  else None
    g    = ws.cell(r, iG).value     if iG     else 1
    hour = ws.cell(r, iHour).value  if iHour  else ''
    phone= ws.cell(r, iPhone).value if iPhone else ''

    if not name or not ci or not co:
        continue
    name_str = str(name).strip()
    if name_str in ('TOTAUX', ''):
        continue

    reservations.append({
        "name":     name_str,
        "checkin":  ci,
        "checkout": co,
        "platform": str(plat or '').strip(),
        "guests":   int(g) if g and str(g).isdigit() else (int(float(str(g))) if g else 1),
        "hour":     str(hour or '').strip(),
        "phone":    str(phone or '').strip(),
    })

print(f"✅ {len(reservations)} reservas encontradas")

with open('reservas.json', 'w', encoding='utf-8') as f:
    json.dump(reservations, f, ensure_ascii=False, indent=2)

print("✅ reservas.json guardado!")
for r in reservations:
    print(f"   {r['plat']} | {r['name']} | {r['ci']} → {r['co']}")
