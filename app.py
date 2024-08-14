
from flask import Flask, request, render_template
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Replace with your Google Books API key
API_KEY = 'AIzaSyDGHyUPzvq7puyujdVZ2oC0J-dJSoZp6Xs'
def fetch_books_from_api(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    books = []
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo', {})
        book = {
            'id': item['id'],
            'title': volume_info.get('title', 'No Title'),
            'authors': ', '.join(volume_info.get('authors', [])),
            'description': volume_info.get('description', 'No Description'),
            'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail', '')
        }
        books.append(book)
    return books

def recommend_books(book_title, books):
    # Extract book titles and descriptions
    titles = [book['title'] for book in books]
    descriptions = [book['description'] for book in books]
    
    # Create a TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(descriptions)
    
    # Calculate similarity
    cosine_similarities = linear_kernel(tfidf_vectorizer.transform([book_title]), tfidf_matrix).flatten()
    
    # Get top 5 book indices
    recommended_indices = cosine_similarities.argsort()[-5:][::-1]
    
    recommended_books = [books[i] for i in recommended_indices]
    return recommended_books

@app.route('/', methods=['GET', 'POST'])
def index():
    similar_books = []
    if request.method == 'POST':
        title = request.form.get('title')
        books = fetch_books_from_api(title)
        similar_books = recommend_books(title, books)
    
    return render_template('index.html', similar_books=similar_books, book_details=similar_books)

if __name__ == '__main__':
    app.run(debug=True)

