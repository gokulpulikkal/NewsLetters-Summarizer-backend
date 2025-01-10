from flask import Flask, request, json
from flask import jsonify
import textwrap
import google.generativeai as genai
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
# Initialize Firebase Admin
cred = credentials.Certificate('firebaseAuth.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

@app.route('/processText', methods=['POST'])
def processText():
    text = request.data.decode('utf-8').strip('```json').strip('```')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Assuming the text is JSON, parse it
        news_data = json.loads(text)

        upload_news_to_firestore(news_data)
        return jsonify({"message": "News uploaded successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def upload_news_to_firestore(news_data):
    # Current date as "YYYY-MM-DD"
    current_date = datetime.now().strftime("%Y-%m-%d")
    news_collection = db.collection("news")

    # Collect all categories
    categories = set(news_item["category"] for news_item in news_data["news"])

    # Reference to the date document
    date_doc_ref = news_collection.document(current_date)

    # Add the categories field to the date document
    date_doc_ref.set({"categories": list(categories)})

    # Add all news items to the date document's collection
    for news_item in news_data["news"]:
        date_doc_ref.collection("newsItems").add({
            "heading": news_item["heading"],
            "detailed_news": news_item["detailed_news"],
            "link": news_item["link"],
            "time_to_read": news_item["time_to_read"],
            "category": news_item["category"],
            "timestamp": firestore.SERVER_TIMESTAMP  # Auto-generated timestamp
        })
    

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)