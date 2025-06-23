from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import pipeline

import zipfile
import os

zip_path = "./output_txt.zip"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall()

folder_path = "output_txt"

documents = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        loader = TextLoader(file_path)
        documents.extend(loader.load())

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(docs, embedding_model)
retriever = vectorstore.as_retriever()

llm_pipeline = pipeline("text-generation", model="gpt2", device=0, max_new_tokens=75)
llm = HuggingFacePipeline(pipeline=llm_pipeline)

prompt_template = "Answer the following question based on the provided context: {context}\n\nQuestion: {query}\nAnswer:"

prompt = PromptTemplate(input_variables=["query", "context"], template=prompt_template)

llm_chain = LLMChain(llm=llm, prompt=prompt)

retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    verbose=True
)

query = "what is Arjuna’s Dilemma?"

# IMPORTANT: using only the top-1 document by default
retrieved_docs = retriever.get_relevant_documents(query)[:1]

context = " ".join([doc.page_content for doc in retrieved_docs])


response = retrieval_qa.run(query)
print("Answer:", response)
