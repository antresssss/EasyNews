import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json
from langchain_google_genai import ChatGoogleGenerativeAI
import pathway as pw

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # NewsAPI key for real-time news
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Google API key for Gemini model

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

promptNews = """
You are a reliable news source that provides fact-checked, concise, and accurate summaries of news topics. 
You respond in a pleasant manner, making the news easy to understand. you provide the latest news first .
Please provide more context to the given topic.
"""

promptJson = """Please convert the given content into a JSON table with keys as numbers and each key has a Title, Content, and Sources.The content is a very brief summary of the title and the remaining information"""

promptQuestion = """You provide concise and fact-checked answers to the given question."""

# Fetching real-time news using NewsAPI
def fetch_real_time_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
       
        news_content = ""
        for idx, article in enumerate(articles[:5], start=1):  # Limit to 5 articles
            title = article['title']
            source = article['source']['name']
            url = article['url']
            
            # Generate enhanced news as a description under the title
            enhanced_news = generate_news(title, promptNews)
            
            news_content += f" **{idx}. {title}** \n {enhanced_news} \n\n Source: {source}\n[Read more]({url})\n\n"
        
        return news_content
    else:
        return "Error fetching real-time news."
def generate_news(topic, prompt):
    response = llm.invoke(prompt + topic)
    return response.content

def create_json(content, promptJson):
    responseJson = llm.invoke(promptJson + content)
    return responseJson.content

# Generate answers based on a question
def generate_answer(question, promptQuestion):
    response = llm.invoke(promptQuestion + question)
    return response.content

st.set_page_config(page_title="Easy News")
st.title("📰 EASY NEWS 📰")

topic = st.text_input("Enter Topic", placeholder="Enter any topic of news 💬")

class InputSchema(pw.Schema):
    Title: str
    Content: str
    Sources: str

if st.button("GET📚"):
    # Fetch real-time news using the NewsAPI
    real_time_news = fetch_real_time_news(topic)
    st.markdown(f"## 🕵️‍♀️ Latest news on {topic}:")
    st.markdown(real_time_news) 

    jsonOfNews = create_json(real_time_news, promptJson)

    try:
        json_data = json.loads(jsonOfNews)

    except json.JSONDecodeError as e:  
        st.markdown(f"# TABLE VIEW :")
        st.write(jsonOfNews)

    if 'json_data' in locals():
        news_table = pw.Table.from_dict(json_data, schema=InputSchema)
        pw.io.jsonlines.write(news_table, "/mnt/data/newsdoc.jsonl")

question = st.text_input("Enter any question", placeholder="ask ❔")
if st.button("Ask Question"):
    if real_time_news:
        answer = generate_answer(question, promptQuestion)
        st.write(answer)
    else:
        st.error("Please generate the news first by entering a topic and clicking the GET button.")
