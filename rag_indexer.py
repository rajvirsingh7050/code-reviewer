from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

def build_repo_vector_store(repo_files: list[dict]) -> FAISS:
    
    all_chunks = []
    
    for file in repo_files:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=file["lang"],
            chunk_size=800,
            chunk_overlap=100
        )
        chunks = splitter.split_text(file["content"])
        for chunk in chunks:
            all_chunks.append(
                Document(
                    page_content=chunk,
                    metadata={"file_path": file["path"]}
                )
            )
            
    vector_store = FAISS.from_documents(all_chunks, embeddings)
    return vector_store