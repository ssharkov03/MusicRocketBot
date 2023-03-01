from typing import Tuple

from bot_text import context
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="Den4ikAI/rubert_large_squad_2",
    tokenizer="Den4ikAI/rubert_large_squad_2"
)


def response_prediction(user_text: str) -> Tuple[str, float]:
    predictions = qa_pipeline({
        'context': context,
        'question': user_text
    })
    predictions['answer'] = predictions['answer'].split("\n")[0].capitalize()
    return predictions['answer'], predictions['score']
