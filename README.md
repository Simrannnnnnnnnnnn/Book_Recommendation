# Book_Recommendation
## Overview 
A web tool called the Book Recommendation System suggests books that are comparable to a user-specified book title. It makes suggestions based on book descriptions by utilizing machine learning techniques and the Google Books API to retrieve book data. This project makes use of the Google Books API for data retrieval, the Flask web framework, and scikit-learn for machine learning.
 
## Features 
-- Book Search: To locate related books, users can enter the title of a book.
-- Book recommendations are made by the system depending on how closely the description matches the supplied book.
-- Book Information: Provides book information, such as the title and authors

## How The Recommendation System Works
-- User input: The title of a book the user likes is entered.
-- Fetch Recommendations: To locate books that are comparable to the input, the system sends a query to the Google Books API.
-- Display Recommendations: A list of suggested books with their titles, authors, and covers is displayed by the system.

## Technologies Used
-- Flask: A web application framework for developing websites.
-- request: HTTP calls to the Google Books API are made using this library.
-- scikit-learn: For computing similarity and analyzing text. Book data, 
such as titles, authors, descriptions, and thumbnails, can be obtained via the Google Books API.

## Setup and Installation 
--clone the Repository 
git clone https://github.com/Simrannnnnnnnnnnn/Book_Recommendation.git

--create a virtual Environment 
python -m venv venv

--Activate The Virutal Environment 
venv\Scripts\activate

--Install Dependencies 
pip install Flask, requests, pandas, scikit-learn

--Configure API key
open 'app.py' and replace the api key with your actual google book api key 

--Run the Application 
python app.py

## Contributing 
Feel free to fork this repository and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## References 
Google Books API Documentation
Flask Documentation
scikit-learn Documentation
TF-IDF Vectorizer - scikit-learn
Linear Kernel - scikit-learn

## Contact 
for questions or feedback, please reach out to kaur.simran1542@gmail.com
