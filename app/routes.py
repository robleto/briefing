from flask import render_template, request, redirect, url_for
from app import app
from app.fetch_headlines import fetch_headlines
from app.summarize_text import summarize_text
from app.email_utils import send_email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    url = request.form.get('url')
    email = request.form.get('email')
    title, text = fetch_headlines(url)
    summary = summarize_text(text)
    body = f"""
    Headline: {title}
    
    Summary:
    {summary}
    """
    send_email(f"Summary for {title}", [email], body)
    return redirect(url_for('home'))
