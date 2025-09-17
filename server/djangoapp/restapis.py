import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Get the backend URL from the environment variables
backend_url = os.getenv(
    "backend_url", "http://localhost:3030")

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """
    Sends a GET request to the specified backend endpoint with optional parameters.
    
    Args:
        endpoint (str): The API endpoint to call.
        **kwargs: Keyword arguments representing URL parameters.
    
    Returns:
        dict or None: The JSON response from the API, or None if an error occurs.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params
    
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    """
    Analyzes the sentiment of a given text using a microservice.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        dict or None: The JSON response from the sentiment analysis service.
    """
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print("Network exception occurred:", e)