from PyPDF2 import PdfReader
import os


# ==========================================
# KNOWLEDGE BASE DIRECTORY
# ==========================================

KNOWLEDGE_BASE_PATH = "rag/knowledge_base"


# ==========================================
# PDF TEXT EXTRACTION FUNCTION
# ==========================================

def extract_pdf_text():

    combined_text = ""

    # LOOP THROUGH ALL FILES

    for file_name in os.listdir(KNOWLEDGE_BASE_PATH):

        # CHECK PDF FILE

        if file_name.endswith(".pdf"):

            pdf_path = os.path.join(
                KNOWLEDGE_BASE_PATH,
                file_name
            )

            print(f"\nProcessing PDF: {file_name}")

            # LOAD PDF

            reader = PdfReader(pdf_path)

            # EXTRACT TEXT FROM ALL PAGES

            for page in reader.pages:

                text = page.extract_text()

                if text:

                    combined_text += text + "\n"

    return combined_text


# ==========================================
# MAIN TEST
# ==========================================

if __name__ == "__main__":

    raw_text = extract_pdf_text()

    print("\n========== EXTRACTED TEXT ==========\n")

    print(raw_text[:5000])