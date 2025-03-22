import gradio as gr
from fetch_news import fetch_news 
from sentiment_model import analyze_sentiment
from summarize_model import summarize_text
from tts import generate_tts

def fetch_and_display_news(company_name):
    news_data = fetch_news(company_name)
    
    if not news_data.get("Articles"):
        return "❌ No news found.", None

    output = f"## 📰 News for {news_data['Company']}:\n\n"
    tts_texts = []
    comparative_data = []
    
    for idx, article in enumerate(news_data["Articles"], start=1):
        title = article.get("Title", "No Title Available")
        content = article.get("Content", "No content available")
        topics = article.get("Topics", ["No topics found"])
        link = article.get("Link", "#") 

        # Analyze sentiment of the content
        sentiment_label, sentiment_score = analyze_sentiment(content)

        sentiment_label = sentiment_label.lower().capitalize() 
        sentiment_score = round(sentiment_score, 2) 

        # Summarize the content
        summary = summarize_text(content) if content else "No summary available."

        output += f"### 🔹 {idx}. {title}  \n**Sentiment**: {sentiment_label} (Confidence: {sentiment_score})\n\n"
        output += f"📝 **Summary**: {summary}\n\n"
        
        topics_str = "No topics found"
        if topics and topics[0] != "No topics found":
            topics_str = ", ".join(topics)

        output += f"🗂 **Topics**: {topics_str}\n"
        output += f"🔗 [Read more]({link})\n\n---\n"

        tts_texts.append(f"लेख {idx}: {title}. भावना: {sentiment_label}. विश्वास: {sentiment_score}. सारांश: {summary}.")

        comparative_data.append({
            "Title": title,
            "Sentiment": sentiment_label,
            "Confidence": sentiment_score,
            "Summary": summary,
            "Topics": topics_str
        })

    # Comparative Analysis
    output += "## 📊 Comparative Analysis\n\n"
    output += "| Title | Sentiment | Confidence | Topics |\n"
    output += "|-------|-----------|------------|--------|\n"
    for data in comparative_data:
        output += f"| {data['Title']} | {data['Sentiment']} | {data['Confidence']} | {data['Topics']} |\n"

    tts_final_text = (
        f"{news_data['Company']} के बारे में समाचार रिपोर्ट का सारांश:\n\n"
        f"कुल लेख: {len(news_data['Articles'])}.\n"
        f"सकारात्मक भावना वाले लेख: {sum(1 for data in comparative_data if data['Sentiment'] == 'Positive')}.\n"
        f"नकारात्मक भावना वाले लेख: {sum(1 for data in comparative_data if data['Sentiment'] == 'Negative')}.\n"
        f"तटस्थ भावना वाले लेख: {sum(1 for data in comparative_data if data['Sentiment'] == 'Neutral')}.\n\n"
        f"मुख्य विषय: {', '.join(set(topic for data in comparative_data for topic in data['Topics'].split(', ')))}.\n"
        )
    tts_audio_path = generate_tts(tts_final_text, lang="hi")

    return output, tts_audio_path

# List of company names for the dropdown
company_names = [
    "Tesla",
    "Apple",
    "Google",
    "Microsoft",
    "Amazon",
    "Meta",
    "NVIDIA",
    "Netflix",
    "Twitter",
    "OpenAI"
]

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🚀 Company News Fetcher")

    with gr.Row():
        company_input = gr.Dropdown(
            label="Select Company",
            choices=company_names,
            value="Tesla" 
        )
        fetch_button = gr.Button("Fetch News")

    news_output = gr.Markdown()
    tts_audio_output = gr.Audio(label="सारांश और भावना सुनें", type="filepath")  # Hindi label

    fetch_button.click(
        fetch_and_display_news,
        inputs=company_input,
        outputs=[news_output, tts_audio_output]
    )

if __name__ == "__main__":
    demo.launch(share=True)