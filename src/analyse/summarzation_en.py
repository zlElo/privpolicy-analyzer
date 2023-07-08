from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import json

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count=2)
    summary = " ".join(str(sentence) for sentence in summary_sentences)
    return summary

def summ_en(file):
    with open(f'data/{file}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    summarized_data = {}
    for key, text in data.items():
        summarized_text = summarize_text(text)
        summarized_data[key] = summarized_text

    with open(f'data/{file}.json', 'w', encoding='utf-8') as f:
        json.dump(summarized_data, f, ensure_ascii=False, indent=4)
