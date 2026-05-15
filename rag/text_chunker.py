from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_processor import extract_pdf_text


# ==========================================
# LOAD RAW PDF TEXT
# ==========================================

raw_text = extract_pdf_text()


# ==========================================
# TEXT SPLITTER CONFIGURATION
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,
    chunk_overlap=100

)


# ==========================================
# CREATE CHUNKS
# ==========================================

chunks = text_splitter.split_text(raw_text)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========== TOTAL CHUNKS ==========\n")

print(len(chunks))


print("\n========== SAMPLE CHUNK ==========\n")

print(chunks[0])