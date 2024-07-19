import requests
from bs4 import BeautifulSoup
import openai
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ensure the environment variable is set
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get the latest ETF news
def get_latest_etf_news():
    url = "https://www.google.com/search?sa=X&sca_esv=4a42ef09a1334cc3&q=latest+etf+news&tbm=nws"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')
    
    news = ""
    for headline in headlines:
        news += headline.text + "\n"
    
    return news

# Function to summarize text using OpenAI API
def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text: {text}"}
        ]
    )
    return response.choices[0].message['content'].strip()

# Function to send email
def send_email(subject, body, to_emails):
    from_email = "your_email@example.com"
    from_password = "your_password"
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, from_password)
        for email in to_emails:
            msg['To'] = email
            server.sendmail(from_email, email, msg.as_string())

if __name__ == "__main__":
    news = get_latest_etf_news()
    summarized_news = summarize_text(news)
    subject = "Daily ETF News Update"
    to_emails = ["your_email@example.com", "colleague1@example.com", "colleague2@example.com"]
    send_email(subject, summarized_news, to_emails)
