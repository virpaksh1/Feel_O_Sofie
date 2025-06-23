# Feel_O_Sofie

# 📚 QA System with LangChain, FAISS, and HuggingFace

This repository contains a Question-Answering (QA) system built using [LangChain](https://github.com/langchain-ai/langchain), [HuggingFace Transformers](https://huggingface.co/docs/transformers), and [FAISS](https://github.com/facebookresearch/faiss). The system extracts information from text files, indexes them using embeddings, and answers user queries based on the most relevant document context.

---

## 🔧 Features

- Extracts and processes `.txt` files from a ZIP archive.
- Splits documents into manageable chunks for indexing.
- Creates vector embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Stores embeddings in a FAISS vector store for efficient retrieval.
- Uses HuggingFace's `gpt2` model for question answering.
- Supports retrieval-augmented generation via LangChain's `RetrievalQA`.

```bash
pip install -r requirements.txt
```

🔧 Note: If you have a CUDA-compatible GPU, you may install faiss-gpu instead of faiss-cpu.

📂 Input Format

Place your .txt files inside a ZIP file named output_txt.zip in the project root directory. The script will automatically extract and process these files.

🧠 How It Works

    Text Extraction: Unzips and reads all .txt files.

    Chunking: Splits documents into overlapping chunks of 500 characters.

    Embedding: Converts text chunks into dense vectors using all-MiniLM-L6-v2.

    Indexing: Stores vectors in FAISS for similarity search.

    Retrieval: Retrieves the most relevant document chunks based on query.

    Answer Generation: Feeds retrieved context and query to a gpt2 model to generate an answer.
    
    
🧪 Usage

To run the script and ask a question:
```bash
python3 src.py
```

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgments

    LangChain

    HuggingFace Transformers

    FAISS by Facebook AI
