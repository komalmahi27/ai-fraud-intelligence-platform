import os

from dotenv import load_dotenv
from openai import OpenAI

from rag.retriever import (
    retrieve_relevant_chunks
)

from rag.prompt_builder import (
    build_copilot_prompt
)

# ==========================================
# LOAD ENV VARIABLES
# ==========================================

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


# ==========================================
# OPENROUTER CLIENT
# ==========================================

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


# ==========================================
# COPILOT RESPONSE FUNCTION
# ==========================================

def generate_copilot_response(
    user_question,
    fraud_analytics,
    ai_recommendations
):

    # ======================================
    # RETRIEVE KNOWLEDGE
    # ======================================

    retrieved_chunks = retrieve_relevant_chunks(
        user_question
    )


    # ======================================
    # BUILD PROMPT
    # ======================================

    final_prompt = build_copilot_prompt(
        user_question,
        retrieved_chunks,
        fraud_analytics,
        ai_recommendations
    )


    # ======================================
    # AI RESPONSE
    # ======================================

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return response.choices[0].message.content