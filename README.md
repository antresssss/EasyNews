# Easy News

📰 Easy News is a web application that leverages the power of RAG (Retrieval-Augmented Generation),Utilizing Google’s Gemini Pro as a Language Model (LLM), prompt engineering, Pathway module, LangChain, and Streamlit to provide users with the latest news on any given topic. The application uses Google Generative AI to generate news content and Pathway to process and display the news data.

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
<video width="600" controls>
  <source src="/EasyNewsDemo.webm" type="video/webm">
</video>

## Technologies Used

- **RAG (Retrieval-Augmented Generation):** Combines retrieval of information with the generation capabilities of large language models to provide more accurate and reliable responses.
- **LLMs (Large Language Models):** Uses Google's Generative AI model, gemini-pro, to generate news content.
- **Prompt Engineering:** Carefully crafted prompts ensure the generation of relevant and accurate news content.
- **Pathway:** Used for data processing and creating a schema for the news data.
- **LangChain:** Facilitates interaction with the large language models.
- **Streamlit:** Provides a user-friendly interface for interaction.

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
    git clone https://github.com/yourusername/easy-news.git
    cd easy-news
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Google API key:

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

5. You can also ask questions related to the news by entering a question in the text input field and clicking on "Ask Question".
