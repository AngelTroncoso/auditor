import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def procesar_normativa_chilena(ruta_pdf):
    print(f"--- Iniciando lectura de: {ruta_pdf} ---")
    
    # 1. Cargar el PDF (SII, NAGAS o IFRS)
    loader = PyPDFLoader(ruta_pdf)
    paginas = loader.load()
    
    # 2. Dividir el texto en fragmentos (Chunks) para el RAG
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    chunks = text_splitter.split_documents(paginas)
    print(f"--- Documento procesado: {len(chunks)} fragmentos generados ---")
    
    return chunks

if __name__ == "__main__":
    pass
