# MindraBot

MindraBot é um assistente inteligente que utiliza inteligência artificial para responder perguntas no Telegram com base em documentos PDF indexados. O projeto foi desenvolvido para facilitar o acesso a informações contidas em arquivos, respondendo de forma rápida e contextualizada via chat.

## Funcionalidades

- **Bot do Telegram:** Interaja com o MindraBot diretamente pelo Telegram.
- **Indexação de PDFs:** Os arquivos PDF são processados e indexados para buscas rápidas e precisas.
- **Respostas Contextuais:** O bot utiliza IA para buscar e responder perguntas com base no conteúdo dos PDFs.
- **Ambiente Docker:** Fácil implantação usando Docker e Docker Compose.
- **Configuração por variáveis de ambiente:** Chaves e tokens são gerenciados via arquivo `.env`.

## Como usar

### 1. Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (opcional, mas recomendado)
- Conta no Telegram para criar um bot e obter o token
- Chave de API da OpenAI

### 2. Configuração

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/vinnyverissimo/MindraBot.git
   cd MindraBot
   ```

2. **Crie o arquivo `.env` com as seguintes variáveis:**
   ```
   OPENAI_API_KEY=your_openai_api_key
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```

3. **Adicione seus arquivos PDF na pasta `files/` (ou conforme configurado em `config.py`).**

### 3. Executando com Docker

1. **Construa e suba o container:**
   ```sh
   docker-compose up --build
   ```

2. O bot será iniciado automaticamente e ficará aguardando mensagens no Telegram.

### 4. Executando localmente (sem Docker)

1. **Crie um ambiente virtual:**
   ```sh
   python -m venv venv
   ```

2. **Ative o ambiente virtual:**
   - No Windows (PowerShell):
     ```sh
     .\venv\Scripts\Activate.ps1
     ```
   - No Windows (cmd):
     ```sh
     .\venv\Scripts\activate.bat
     ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Execute o bot:**
   ```sh
   python botTelegram.py
   ```

## Estrutura do Projeto

```
MindraBot/
│
├── botTelegram.py        # Código principal do bot Telegram
├── indexing.py           # Indexação e busca nos PDFs
├── chat_engine.py        # Lógica de resposta do bot
├── config.py             # Configurações e variáveis globais
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # Dockerfile para build da imagem
├── docker-compose.yml    # Orquestração com Docker Compose
├── files/                # Pasta para armazenar PDFs
└── .env                  # Variáveis de ambiente (NÃO versionar)
```

## Observações

- Certifique-se de que os arquivos PDF estejam legíveis e sem caracteres corrompidos.
- O projeto utiliza a biblioteca [python-telegram-bot](https://python-telegram-bot.org/) e [LangChain](https://python.langchain.com/).
- Para dúvidas sobre tokens e configuração, consulte a documentação oficial do [Telegram Bots](https://core.telegram.org/bots) e [OpenAI](https://platform.openai.com/docs/api-reference).

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por