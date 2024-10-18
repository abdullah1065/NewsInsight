import json
from NewsInsight.scraper import scrape_urls, scrape_article_data
from NewsInsight.llm_analyzer import analyze_articles

def main():
    category_url = 'https://samakal.com/economics' 
    article_urls = scrape_urls(category_url)

    scrape_articles_data = []
    for url in article_urls:
        scrape_articles_data.append(scrape_article_data(url))

    with open('scraped_news_raw.json', 'w', encoding='utf-8') as f:
        json.dump(scrape_articles_data, f, ensure_ascii=False, indent=4)

    analyze_articles()

    print("Sentiment analysis results have been saved to 'analyzed_news.json'.")

# Run the main function
if __name__ == "__main__":
    main()