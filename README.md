# Easy News

📰 Easy News is a web application that leverages the power of RAG (Retrieval-Augmented Generation),Utilizing Google’s Gemini Pro as a Language Model (LLM), prompt engineering,the Pathway module(a Python data processing framework for analytics and AI pipelines over data streams), LangChain, and Streamlit to provide users with the latest news on any given topic. The application uses Google Generative AI to generate news content and Pathway to process and display the news data in a tabular format.

**there are two files app.py and app_rework.py,latter is the one which utilizes the News API**

## Features

- **Fact-checked News:** Provides fact-checked, accurate, and reliable news.
- **Latest Updates:** Ensures the news updates are recent and up-to-date.
- **Google’s Gemini Pro**: Utilizes the powerful Gemini Pro model for generating news summaries and answering questions.
- **Customizable Topics:** Users can input any topic to get the latest news related to it.
- **Question Answering:** Users can ask questions related to the generated news.
- **JSON Conversion:** Converts news content into a structured JSON format.
- **Data Processing with Pathway:** Uses Pathway to store and process the news data.
- **User Interface with Streamlit:** Provides an easy-to-use interface built with Streamlit.

## Demo

https://github.com/user-attachments/assets/e42f7a8e-522c-4914-b7ed-d30959c5f7fd

## Technologies Used

- **RAG (Retrieval-Augmented Generation):** Combines retrieval of information with the generation capabilities of large language models to provide more accurate and reliable responses.
- **News API:** News API is a simple, easy-to-use REST API that returns JSON search results for current and historic news articles published by over 150,000 worldwide sources.
- **LLMs (Large Language Models):** Uses Google's Generative AI model, gemini-pro, to generate news content.
- **Prompt Engineering:** Carefully crafted prompts ensure the generation of relevant and accurate news content.
- **Pathway:** Used for data processing and creating a schema for the news data.
- **LangChain:** Facilitates interaction with the large language models.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Pathway
- dotenv
- langchain_google_genai

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/antresssss/EasyNews
    cd EasyNews
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Google API key(assuming you have generated one, if not then search up on how to create one):

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

### Usage

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your browser and go to [http://localhost:8501](http://localhost:8501).

3. Enter the topic for which you want the latest news in the text input field and click on "GET📚".

4. The latest news on the entered topic will be displayed along with a data table.

5. You can also ask questions related to the news or if you are curious about just anything by entering a question in the text input field and clicking on "Ask Question".

## end notes

this is a simple app I made during the PathwayXGenAI bootcamp , I am grateful for the lessons and the task or opportunity to be able to create an app from it . Thank you for reading this far :D