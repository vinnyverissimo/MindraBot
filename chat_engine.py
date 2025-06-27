from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chat = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.2)
# chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2)


def carregar_prompt(nome_arquivo):
    with open(nome_arquivo, encoding="utf-8") as f:
        return f.read()


def resposta_bot(pergunta, contexto, max_retries=3):
    prompt_template = carregar_prompt("prompt_pt.txt")

    mensagem_system = prompt_template.format(contexto=contexto)

    mensagens_modelo = [('system', mensagem_system), ('user', pergunta)]
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    import time
    for retry in range(max_retries):
        try:
            return chain.invoke({}).content
        except Exception as e:
            print(
                f"Erro na chamada da API (tentativa {retry + 1}/{max_retries}): {e}")
            if retry < max_retries - 1:
                time.sleep(2 ** retry)
            else:
                return "Desculpe, não consegui obter uma resposta da API após várias tentativas."
