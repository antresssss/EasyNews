import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import pathway as pw
import json

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

promptNews = """You are a reliable news source. You always provide fact-checked, accurate, and reliable news on a topic. You respond in a pleasant manner, making the news easy to understand, and you cite multiple sources. Please provide the latest news updates on the given topic, prioritizing the most recent information first.
topic:technology

1.AI advancements: News outlets might be buzzing about Google's recent integration of AI into their search engine, promising better results but also raising concerns about reduced web traffic for some sites. (https://www.thehindu.com/sci-tech/technology/google-deepmind-ai-reveals-potential-for-thousands-of-new-materials/article67589647.ece)
2.Breakthrough in brain-computer interfaces: There could be reports on researchers successfully developing a device that translates brain thoughts into real-time text. This has huge implications for communication accessibility but also ethical considerations. (https://www.facebook.com/photo.php?fbid=827791859384364&id=100064606727322&set=a.353284630168425)

Please provide latest news of the topic given here:
"""

promptJson = """please convert the given content into a json table with keys as numbers and each key has a Title,Content and Sources. Expand the body with valid information regarding the heading.
content:
"""

promptQuestion = """you provide concise and fact checked answer to the given question """

def generate_answer(question, context, promptQuestion):
    response = llm.invoke(promptQuestion + context + question)
    return response.content

def generate_news(topic, prompt):
    response = llm.invoke(prompt + topic)
    return response.content

def create_json(content, promptJson):
    responseJson = llm.invoke(promptJson + content)
    return responseJson.content

st.set_page_config(page_title="Easy News")
st.title("📰 EASY NEWS 📰")
topic = st.text_input(" Enter Topic ", placeholder=" Enter any topic of news 💬 ")

class InputSchema(pw.Schema):
    Title: str
    Content: str
    Sources: str

news_final = ""
jsonOfNews = ""

if st.button("GET📚"):
    news_final = generate_news(topic, promptNews)
    st.markdown(f"## 🕵️‍♀️ Latest news on {topic} :")
    st.write(news_final)

    jsonOfNews = create_json(news_final, promptJson)

    # Validate and parse the JSON string
    try:
        json_data = json.loads(jsonOfNews)
    except json.JSONDecodeError as e:
        ##st.error(f"JSON decode error: {e}")
        st.markdown(f"# TABLE VIEW :")
        st.write(jsonOfNews)

    # Use Pathway to store and process the news data if json_data is valid
    if 'json_data' in locals():
        news_table = pw.Table.from_dict(json_data, schema=InputSchema)
        pw.io.jsonlines.write(news_table, "/mnt/data/newsdoc.jsonl")


question = st.text_input("Enter any question  ", placeholder="ask ❔ ")
if st.button("Ask Question"):
    answer = generate_answer(question, news_final, promptQuestion)
    if answer:
        st.write(answer)
    else:
        st.error("Please generate the news first by entering a topic and clicking the GET button.")
