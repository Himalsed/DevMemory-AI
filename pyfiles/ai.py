import ollama


def generate_answer(context, question):
    """
    Generate answer using local Llama model.
    """

    prompt = f"""
You are DevMemory AI, an AI coding assistant.
Use the code context below to answer.
Rules:
- Mention file names.
- Explain clearly.
- Do not invent information.
CODE CONTEXT:

{context}



QUESTION:
{question}

Answer:
"""
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]
