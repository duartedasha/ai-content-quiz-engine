def quiz_prompt(text_chunk):

    prompt = f"""
You are an educational quiz generator.

From the following content generate exactly 3 quiz questions.

Content:
{text_chunk}

Rules:
- Output MUST be valid JSON
- No explanation
- No text outside JSON

Format:

[
{{
"question": "string",
"type": "MCQ | TRUE_FALSE | FILL_BLANK",
"options": ["A","B","C","D"],
"answer": "correct answer",
"difficulty": "easy"
}}
]

If the question type is TRUE_FALSE or FILL_BLANK, options can be empty.
"""

    return prompt