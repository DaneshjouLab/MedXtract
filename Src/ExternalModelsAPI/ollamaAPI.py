from baseAPI import baseAPI

import numpy as np
# ultimately you take in a messge

class ollamaAPI():
    def __init__(self):

        pass

    def fmt(self):
        """
        builds formatting for the models.... 
        # ok 
        _____
        """
        pass
    
import http.client
import json
import http.client
import json

def chat_with_model(host, port, path, data):
    """
    Function to make a POST request to the specified host and port, and chat with the model.

    Args:
        host (str): The hostname of the server.
        port (int): The port number of the server.
        path (str): The API endpoint path.
        data (dict): The data payload for the POST request.

    Returns:
        dict: The response from the server.
    """
    # Convert the data to JSON
    json_data = json.dumps(data)

    # Create a connection to the server
    conn = http.client.HTTPConnection(host, port)

    # Define the headers
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    conn.request("POST", path, body=json_data, headers=headers)

    # Get the response
    response = conn.getresponse()

    # Read and decode the response data
    response_data = response.read().decode()

    # Close the connection
    conn.close()

    # Return the response as a JSON object
    return json.loads(response_data)
import http.client
import json

def get_embeddings(host, port, path, data):
    """
    Function to make a POST request to the specified host and port, and retrieve embeddings.

    Args:
        host (str): The hostname of the server.
        port (int): The port number of the server.
        path (str): The API endpoint path.
        data (dict): The data payload for the POST request.

    Returns:
        dict: The response from the server.
    """
    # Convert the data to JSON
    json_data = json.dumps(data)

    # Create a connection to the server
    conn = http.client.HTTPConnection(host, port)

    # Define the headers
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    conn.request("POST", path, body=json_data, headers=headers)

    # Get the response
    response = conn.getresponse()

    # Read and decode the response data
    response_data = response.read().decode()

    # Close the connection
    conn.close()

    # Return the response as a JSON object
    return json.loads(response_data)
def cosine_similarity(vec1, vec2):
    """
    Function to calculate cosine similarity between two vectors.

    Args:
        vec1 (list or np.array): The first vector.
        vec2 (list or np.array): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# Example usage:
host = "localhost"
port = 11434

# Get the first embedding
path_embeddings = "/api/embeddings"
data1 = {
    "model": "llama3",
    "prompt": "I am testing something with embeddings",
    "stream": False
}
embedding1 = get_embeddings(host, port, path_embeddings, data1)["embedding"]

# Get the second embedding
data2 = {
    "model": "llama3",
    "prompt": "I am testing, my embeddings something with embeddings",
    "stream": False
}
embedding2 = get_embeddings(host, port, path_embeddings, data2)["embedding"]

# Calculate cosine similarity
similarity = cosine_similarity(embedding1, embedding2)
print(f"Cosine similarity: {similarity}")



import requests
from bs4 import BeautifulSoup
import re
# Function to fetch and parse content from a URL with headers
def fetch_text_from_url(url):
    # Define headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check that the request was successful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text from the parsed HTML
    text_content = soup.get_text()

    return text_content

# URL to fetch content from
def replace_multiple_newlines(text):
    return re.sub(r'\n{3,}', '\n\n', text)

# URL to fetch content from
url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8485851/"

# Fetch the content
content = fetch_text_from_url(url)

# Replace multiple newlines with a maximum of two
cleaned_content = replace_multiple_newlines(content)
print(cleaned_content)  # Print the first 2000 characters to check

data3 = {
    "model": "llama3",
    "prompt": cleaned_content,
    "stream": False
}
url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10315776/"

# Fetch the content
content = fetch_text_from_url(url)

# Replace multiple newlines with a maximum of two
cleaned_content2 = replace_multiple_newlines(content)
data4 = {
    "model": "llama3",
    "prompt": cleaned_content2,
    "stream": False
}

embedding3 = get_embeddings(host, port, path_embeddings, data3)["embedding"]
embedding4 = get_embeddings(host, port, path_embeddings, data4)["embedding"]

similarity = cosine_similarity(embedding3, embedding4)
print(f"Cosine similarity: {similarity}")


