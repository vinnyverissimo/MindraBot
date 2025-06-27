import os
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config import PDF_DIR

INDEX_PATH = "faiss_index"


def remove_caracteres_invalidos(texto):
    # Remove caracteres surrogates e não imprimíveis
    return re.sub(r'[\ud800-\udfff]', '', texto)


def cria_indice():
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(
            INDEX_PATH,
            OpenAIEmbeddings(),
            allow_dangerous_deserialization=True
        )
    documentos = []
    for nome_arquivo in os.listdir(PDF_DIR):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho = os.path.join(PDF_DIR, nome_arquivo)
            loader = PyPDFLoader(caminho)
            try:
                lista_documentos = loader.load()
            except Exception as e:
                print(f"Erro ao carregar '{caminho}': {e}")
                continue
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000, chunk_overlap=200)
            for doc in lista_documentos:
                # Limpa caracteres inválidos antes de dividir
                conteudo_limpo = remove_caracteres_invalidos(doc.page_content)
                try:
                    textos_divididos = text_splitter.split_text(conteudo_limpo)
                    documentos.extend([Document(page_content=texto)
                                      for texto in textos_divididos])
                except Exception as e:
                    print(
                        f"Erro ao dividir texto do documento '{caminho}': {e}")
                    continue
    embeddings = OpenAIEmbeddings()
    indice = FAISS.from_documents(documentos, embeddings)
    indice.save_local(INDEX_PATH)
    return indice


def busca_contexto(indice, pergunta, k=30):
    resultados = indice.similarity_search(pergunta, k=k)
    return "\n".join([resultado.page_content for resultado in resultados])
