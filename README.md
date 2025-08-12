# Enviador de Mensagem de WhatsApp - Supabase + Z-API

Sistema para envio automatizado de mensagens WhatsApp usando contatos armazenados no Supabase e enviando via Z-API.

## 🚀 Começando

### Pré-requisitos

- Python 3.10+
- Conta no [Supabase](https://supabase.com/)
- Conta no [Z-API](https://z-api.io/)

### 🔧 Configuração

1. **Banco de dados Supabase**
    - Crie uma tabela `contacts` com campos:
        - `id` (uuid, primary key)
        - `name` (text)
        - `phone` (text) - formato: 5511999999999 (código país + DDD + número)
        - Insira dados de teste

2. **Z-API**
    - Obtenha seu token e instance ID no painel

3. **Variáveis de Ambiente**
    ```bash
    cp .env.example .env
    ```
    Preencha o arquivo `.env` com suas credenciais: 
    ```ini
    # Supabase
    SUPABASE_URL=sua_url_do_supabase
    SUPABASE_KEY=sua_chave_anon_public
    
    # Z-API
    ZAPI_TOKEN=seu_token
    ZAPI_INSTANCE=sua_instancia
    ```
### 🛠️ Instalação

1. **Clone o repositório**
    ```bash
    git clone https://github.com/Sorridentes/send-supabase-zapi.git
    cd whatsapp-supabase-zapi
    ```

2. **Crie um ambiente virtual (opcional)**
    ```bash
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate #Windows
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
### ▶️ Execução
    ```bash
    python -m src.main

