# News Summarization and Text-to-Speech Application

A web-based application that extracts key details from news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a Hindi text-to-speech (TTS) output. The tool allows users to input a company name and receive a structured sentiment report along with an audio summary.

## Features
- **News Extraction**: Scrapes and displays titles, summaries, and metadata from 10+ news articles using BeautifulSoup.
- **Sentiment Analysis**: Classifies article content as positive, negative, or neutral.
- **Comparative Analysis**: Compares sentiment across articles to derive insights on news coverage.
- **Hindi TTS**: Converts summarized content into Hindi speech using the **Google Text-to-Speech (TTS) API**.
- **User Interface**: Simple web interface built with Gradio for user input and report generation.
- **API Integration**: Frontend and backend communication via APIs.
- **Deployment**: Deployed on Hugging Face Spaces for easy access and testing.

## Technologies Used
- **Python**: For backend logic, scraping, and analysis.
- **BeautifulSoup**: For web scraping.
- **Hugging Face Transformers**: For sentiment analysis and summarization.
- **Gradio**: For the web interface.
- **Google Text-to-Speech (TTS) API**: For generating Hindi speech.

## How to Use

Follow these steps to set up and run the **News Summarization and Text-to-Speech Application** on your local machine.

### Prerequisites
- Python 3.8 or higher installed on your system.
- A valid **Google Cloud API key** for the Google Text-to-Speech (TTS) API. You can get one from the [Google Cloud Console](https://console.cloud.google.com/).

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/darshankathiravan/News-Summarization-with-sentiment-Analysis.git
```
### Step 2: Navigate to the Project Directory
Change to the project directory:
```bash
cd news-summarization-tts
```
### Step 3: Install Dependencies
Install the required Python packages using the requirements.txt file:
```bash
pip install -r requirements.txt
```
### Step 4: Set Up Google TTS API Key
1. Create a `.env` file in the root directory of the project.
2. Add your Google Cloud API key to the `.env` file as follows:
   ```plaintext
   
   GOOGLE_API_KEY=your_api_key_here
   
### Step 5: Run the Application
``` bash
python app.py
```
### Check the output in your gradio url
---
### Check the live link here:
```bash
https://huggingface.co/spaces/kathiravandarshan/News_Summarizer
```
### **How to Update the README.md**
1. Copy the above content.
2. Open your GitHub repository.
3. Edit the `README.md` file.
4. Replace the **How to Use** and **Documentation** sections with the updated content.
5. Commit the changes.

---



