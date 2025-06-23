import os
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def split_into_sentences(text):
    # Basic sentence tokenizer using regular expressions
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]

def write_sentences_to_files(sentences, output_folder, file_counter):
    for i in range(0, len(sentences), 10):
        chunk = sentences[i:i + 10]
        output_filename = f"output{file_counter}.txt"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(' '.join(chunk))

        print(f"Created: {output_filename}")
        file_counter += 1
    return file_counter

def process_pdfs(input_folder, output_folder, num_files):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    pdf_files.sort()  # Ensure consistent order

    file_counter = 1  # To name output files like output1.txt, output2.txt, etc.

    for pdf_file in pdf_files[:num_files]:
        pdf_path = os.path.join(input_folder, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        sentences = split_into_sentences(text)
        file_counter = write_sentences_to_files(sentences, output_folder, file_counter)

# === Configuration ===
input_folder = "/home/virpaksh/Feel_o_sofi/pdf_dir/"        # Folder where your PDF files are
output_folder = "/home/virpaksh/Feel_o_sofi/output_txt/"    # Folder where the output .txt files will go
num_files = 2              # Number of PDF files to process

process_pdfs(input_folder, output_folder, num_files)

