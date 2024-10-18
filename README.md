# NewsInsight

It scrapes news articles from the web, analyzes their sentiment, generates news scores, and identifies whether the article has an international perspective. 

## Features

- **News Scraping**: Extracts news articles from specified news portals.
- **Sentiment Analysis**: Uses a pre-trained LLM model to classify news sentiment as `Positive`, `Neutral`, or `Negative`.
- **News Scoring**: Generates a score based on the length and relevance of the article.
- **International Perspective**: Determines if the article discusses global or international issues.
- **JSON Output**: Saves the analyzed data in a structured JSON format.

## Project Structure

```bash
├── NewsInsight
│   ├── scraper.py              # Script for scraping news articles
│   ├── llm_analyzer.py             # Script for analyzing the articles
│   └── utils.py   
├── main.py   
├── scraped_news_raw.json   
├── analyzed_news.json              # Test scripts for validating functionalities
├── .gitignore                  # Git ignore file
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/NewsInsight.git
    cd NewsInsight
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your API keys (e.g., LLM, scraping API) as environment variables or in a `.env` file.

## Usage

1. **Analyzing News Articles**:
   After scraping, use the analyzer script to process the news content.

    ```bash
    python main.py
    ```

3. **Saving Analyzed Data**:
   The analyzed data, including sentiment, score, and international perspective, will be saved in `analyzed_news.json`.

## Example Output

A typical output in the `analyzed_news.json` file would look like:

```json
{
   "title": "অপচয় ও দুর্নীতি প্রতিরোধে অটোমেটেড সেবা গুরুত্বপূর্ণ: অর্থ উপদেষ্টা",
    "url": "https://samakal.com/economics-others/article/258276/%E0%A6%85%E0%A6%AA%E0%A6%9A%E0%A7%9F-%E0%A6%93-%E0%A6%A6%E0%A7%81%E0%A6%B0%E0%A7%8D%E0%A6%A8%E0%A7%80%E0%A6%A4%E0%A6%BF-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF%E0%A6%B0%E0%A7%8B%E0%A6%A7%E0%A7%87-%E0%A6%85%E0%A6%9F%E0%A7%8B%E0%A6%AE%E0%A7%87%E0%A6%9F%E0%A7%87%E0%A6%A1-%E0%A6%B8%E0%A7%87%E0%A6%AC%E0%A6%BE-%E0%A6%97%E0%A7%81%E0%A6%B0%E0%A7%81%E0%A6%A4%E0%A7%8D%E0%A6%AC%E0%A6%AA%E0%A7%82%E0%A6%B0%E0%A7%8D%E0%A6%A3:-%E0%A6%85%E0%A6%B0%E0%A7%8D%E0%A6%A5-%E0%A6%89%E0%A6%AA%E0%A6%A6%E0%A7%87%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A6%BE",
    "content": "অর্থ উপদেষ্টা ড. সালেহউদ্দিন আহমেদ বলেন, অপচয় ও দুর্নীতি প্রতিরোধে অটোমেটেড সরকারি আর্থিক সেবা গুরুত্বপূর্ণ ভূমিকা পালন করছে। আর্থিক সেবার বিভিন্ন প্লাটফর্ম একটি সমন্বিত ব্যবস্থাপনার মধ্যে নিয়ে আনা সম্ভব হলে আর্থিক ব্যবস্থাপনায় স্বচ্ছতা ও জবাবদিহিতা নিশ্চিত করা সম্ভব হবে। সাধারণ মানুষ সেবা প্রদানকারীর কাছে না গিয়ে যত বেশি সেবা অটোমেটেড পদ্ধতিতে পাবেন ততই দুর্নীতি কমবে।\nসোমবার অর্থ বিভাগের বিভিন্ন সেবা দ্রুততার সঙ্গে সহজে ও সাশ্রয়ীভাবে প্রদানের জন্য তৈরি করা বিভিন্ন অনলাইন প্ল্যাটফর্ম উদ্বোধন করেন অর্থ উপদেষ্টা আজ। তিনি  বলেন, উদ্ভাবিত বিভিন্ন অটোমেটেড সেবা প্লাটফর্মের কার্যকারিতা সমুন্নত রাখার জন্য দক্ষ জনবল সৃষ্টি করে তাদের মাধ্যমে নিয়মিত নবায়ন করতে হবে।\nউদ্বোধন করা সেবাসমূহের মধ্যে রয়েছে- নবরূপায়িত আইবাস++ ওয়েবসাইট, এ-চালান ওয়েবসাইট, পেনশনারদের জন্য লাইফ ভেরিফিকেশন অ্যাপ, পেপারলেস অনলাইন লাস্ট পেমেন্ট সার্টিফিকেট (এলপিসি), সরকারি কর্মচারীদের অনলাইনে ছুটির আবেদন দাখিল, ছুটি মঞ্জুর ও হিসাবায়নের জন্য অনলাইন ছুটি ব্যবস্থাপনা,  অনলাইনভিত্তিক সরকারি আবাসন না-দাবি সনদপত্র এবং সরকারি কর্মচারীদের বেতন-ভাতার বিল দাখিল ও চাকরি সংক্রান্ত অন্যান্য তথ্য অনলাইনে পাওয়ার সুবিধার জন্য ‘আইবাস সেইফ’ মোবাইল অ্যাপ।\nঅনুষ্ঠানের বিশেষ অতিথি হিসেবে উপস্থিত ছিলেন বাংলাদেশ কম্পট্রোলার এন্ড অডিটর জেনারেল মো. নূরুল ইসলাম, প্রধান উপদেষ্টার কার্যালয়ের সচিব মো. সাইফুল্লাহ পান্না, অভ্যন্তরীণ সম্পদ বিভাগের সচিব ও জাতীয় রাজস্ব বোর্ডের চেয়ারম্যান আবদুর রহমান খান ও অর্থনৈতিক সম্পর্ক বিভাগ শাহ্‌রিয়ার কাদের ছিদ্দিকী।\n অর্থ সচিব ড. মো. খায়েরুজ্জামান মজুমদারের সভাপতিত্বে সভায় অর্থ বিভাগের স্ট্রেনদেনিং পাবলিক ফাইনানসিয়াল ম্যানেজমেন্ট টু এনাবেল সার্ভিস ডেলিভারি (এসপিএফএমএস) কর্মসূচির আওতায় প্রস্তুত করা বিভিন্ন অনলাইন সেবার ওপর উপস্থাপনা করেন অর্থ বিভাগের অতিরিক্তি সচিব ও এসপিএফএমএস কর্মসূচির জাতীয় কর্মসূচি পরিচালক মোহাম্মদ সাইফুল ইসলাম।",
    "sentiment": "Positive",
    "news_score": "8",
    "is_international": false
}
```


