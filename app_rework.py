import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json
from langchain_google_genai import ChatGoogleGenerativeAI
import pathway as pw

# Load environment variables
load_dotenv()

# API keys from .env file
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # NewsAPI key for real-time news
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Google API key for Gemini model

# Initialize Google Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# Prompt for news content
promptNews = """
You are a reliable news source that provides fact-checked, concise, and accurate summaries of news topics. 
You respond in a pleasant manner, making the news easy to understand. 
Please provide more context to the given topic.
"""

# Prompt to convert content into JSON format
promptJson = """Please convert the given content into a JSON table with keys as numbers and each key has a Title, Content, and Sources.The content is a very brief summary of the title and the remaining information"""

# Prompt for answering questions
promptQuestion = """You provide concise and fact-checked answers to the given question."""

# Fetch real-time news using NewsAPI
def fetch_real_time_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        
        # Format news content with Markdown for better display
        news_content = ""
        for idx, article in enumerate(articles[:5], start=1):  # Limit to 5 articles
            title = article['title']
            source = article['source']['name']
            url = article['url']
            
            # Generate enhanced news as a description under the title
            enhanced_news = generate_news(title, promptNews)
            
            # Combine the title and enhanced news into the content
            news_content += f" **{idx}. {title}** \n {enhanced_news} \n\n Source: {source}\n[Read more]({url})\n\n"
        
        return news_content
    else:
        return "Error fetching real-time news."

# Generate enhanced news response using Gemini
def generate_news(topic, prompt):
    response = llm.invoke(prompt + topic)
    return response.content

# Create JSON from news content using the Gemini model
def create_json(content, promptJson):
    responseJson = llm.invoke(promptJson + content)
    return responseJson.content

# Generate answers based on a question
def generate_answer(question, context, promptQuestion):
    response = llm.invoke(promptQuestion + context + question)
    return response.content

# Streamlit UI setup
st.set_page_config(page_title="Easy News")
st.title("📰 EASY NEWS 📰")

# Input for topic
topic = st.text_input("Enter Topic", placeholder="Enter any topic of news 💬")

# Class definition for Pathway data schema
class InputSchema(pw.Schema):
    Title: str
    Content: str
    Sources: str

# Button to get news
if st.button("GET📚"):
    # Fetch real-time news using the NewsAPI
    real_time_news = fetch_real_time_news(topic)
    st.markdown(f"## 🕵️‍♀️ Latest news on {topic}:")
    st.markdown(real_time_news)  # Displaying news with proper formatting

    # Generate JSON content from enhanced news
    jsonOfNews = create_json(real_time_news, promptJson)

    # Validate and parse the JSON string
    try:
        json_data = json.loads(jsonOfNews)

    except json.JSONDecodeError as e:  
        st.markdown(f"# TABLE VIEW :")
        st.write(jsonOfNews)
    # Use Pathway to store and process the news data if JSON is valid
    if 'json_data' in locals():
        news_table = pw.Table.from_dict(json_data, schema=InputSchema)
        pw.io.jsonlines.write(news_table, "/mnt/data/newsdoc.jsonl")

# Question input and response
question = st.text_input("Enter any question", placeholder="ask ❔")
if st.button("Ask Question"):
    if real_time_news:
        answer = generate_answer(question, real_time_news, promptQuestion)
        st.write(answer)
    else:
        st.error("Please generate the news first by entering a topic and clicking the GET button.")
