from dotenv import load_dotenv
from groq import Groq
import os
import json

from .utils import extract_info

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)




def analyze_article_with_llm(content):
    prompt = (
    f"Please analyze the following news article:\n\n"
    f"1. Generate a score for the content (Provide just score out of 10).\n"
    f"2. Provide the sentiment as a single word ('Positive', 'Neutral', or 'Negative').\n"
    f"3. Indicate whether the article has an international perspective (True/False).\n\n"
    f"News Article:\n{content}"
)
    
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-70b-8192",
)


    generated_text = chat_completion.choices[0].message.content

    sentiment, score, international_perspective = extract_info(generated_text)

    return sentiment, score, international_perspective


def analyze_articles():

    with open('scraped_news_raw.json', 'r', encoding='utf-8') as file:
        articles = json.load(file)


    analyzed_articles = []


    for article in articles:
        content = article.get('content', '')
        sentiment, news_score, international = analyze_article_with_llm(content[:512])

        analyzed_articles.append({
            'title': article.get('title'),
            'url': article.get('url'),
            'content': content,
            'sentiment': sentiment,
            'news_score': news_score,
            'is_international': international
        })

    with open('analyzed_news.json', 'w', encoding='utf-8') as output_file:
        json.dump(analyzed_articles, output_file, ensure_ascii=False, indent=4)
