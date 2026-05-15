# ==========================================
# PROMPT BUILDER FUNCTION
# ==========================================

def build_copilot_prompt(

    user_question,
    retrieved_chunks,
    fraud_analytics,
    ai_recommendations

):

    # ======================================
    # FORMAT RETRIEVED KNOWLEDGE
    # ======================================

    retrieved_context = "\n\n".join(
        retrieved_chunks
    )

    # ======================================
    # BUILD FINAL PROMPT
    # ======================================

    prompt = f"""

You are an Enterprise Fraud Intelligence AI Copilot.

Your role is to assist fraud investigators,
risk analysts, compliance teams,
and financial intelligence officers.

Use BOTH:

1. Enterprise fraud policy knowledge
2. Live fraud intelligence analytics

to answer the user professionally.


==================================================
USER QUESTION
==================================================

{user_question}


==================================================
RETRIEVED FRAUD POLICY KNOWLEDGE
==================================================

{retrieved_context}


==================================================
LIVE FRAUD ANALYTICS
==================================================

{fraud_analytics}


==================================================
AI RECOMMENDATIONS
==================================================

{ai_recommendations}


==================================================
INSTRUCTIONS
==================================================

Provide:
- fraud investigation guidance
- compliance insights
- risk interpretation
- operational recommendations

Be professional and concise.

"""

    return prompt