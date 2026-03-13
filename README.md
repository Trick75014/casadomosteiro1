# 🏠 Casa do Mosteiro — Calendário

Site web de gestão de reservas com atualização automática.

---

## 📋 Ficheiros

| Ficheiro | Função |
|---|---|
| `index.html` | Site web do calendário |
| `reservas.json` | Dados das reservas (gerado automaticamente) |
| `convert.py` | Script de conversão Excel → JSON |
| `Casa_do_Mosteiro_v6.xlsx` | Excel principal (**é este que edita**) |
| `.github/workflows/update.yml` | Automação GitHub |

---

## 🚀 Configuração inicial (uma única vez)

### 1. Criar o repositório no GitHub
1. Ir a [github.com/new](https://github.com/new)
2. Nome: `casa-mosteiro`
3. Marcar **Public** ✅
4. Clicar **Create repository**

### 2. Carregar os ficheiros
Arrastar todos estes ficheiros para o repositório:
- `index.html`
- `reservas.json`
- `convert.py`
- `Casa_do_Mosteiro_v6.xlsx`
- Pasta `.github/` (com o ficheiro `workflows/update.yml` dentro)

### 3. Ativar GitHub Pages
1. No repositório → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **(root)**
4. Clicar **Save**

⏳ Aguardar ~2 minutos → o site fica disponível em:
**`https://SEU-UTILIZADOR.github.io/casa-mosteiro`**

Enviar este link para o grupo WhatsApp 🎉

---

## 🔁 Atualizar reservas (uso diário)

1. Abrir o Excel `Casa_do_Mosteiro_v6.xlsx` no computador
2. Adicionar/editar as reservas
3. Guardar o ficheiro
4. Ir ao repositório GitHub → clicar no ficheiro Excel → **pencil icon** → Upload novo ficheiro
5. ✅ Em 1-2 minutos o site atualiza automaticamente

---

## 📱 Fluxo completo

```
Edita Excel → Carrega no GitHub → GitHub converte → Site atualiza → WhatsApp vê
```

---

## ❓ Dúvidas

Enviar o Excel atualizado ao assistente Claude para gerar um novo zip pronto a carregar.
