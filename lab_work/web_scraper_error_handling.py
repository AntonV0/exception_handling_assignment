"""Team Lab Work: Build a Web Scraper Using Requests"""
import requests

# Program should prompt user for a URL
url = input("Enter a URL: ").strip()
# Ensure the URL starts with http:// or https://
if not url.startswith(("http://", "https://")):
    url = "https://" + url

# Make a GET request to the URL with error handling
response = requests.get(url, timeout=10) # Set a timeout for the request
try:
    response.raise_for_status()  # Raise an error for bad responses
    print("Web page content:")
    print(response.text)  # Print the content of the web page
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # HTTP error
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")  # Timeout error
except requests.exceptions.TooManyRedirects:
    print("Too many redirects. Please check the URL and try again.")  # Too many redirects error
except requests.exceptions.SSLError:
    print("SSL error occurred. Please check the URL and try again.")  # SSL error
except requests.exceptions.ConnectionError:
    print("Connection error occurred. Please check your internet connection and the URL.")
    # Connection error
except requests.exceptions.URLRequired:
    print("A valid URL is required. Please check the URL and try again.")  # URL required error
except requests.exceptions.ContentDecodingError:
    print("Content decoding error occurred. Unable to decode the response content.")  # Content decoding error
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")  # Other request errors

# Example outputs:
# Enter a URL: google
# raise ConnectionError(e, request=request)
# requests.exceptions.ConnectionError: HTTPSConnectionPool(host='google', port=443): 
# Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection
# (host='google', port=443): Failed to resolve 'google' ([Errno 11001] getaddrinfo failed)"))

# Enter a URL: https://www.google.com
# Outputs the HTML content of Google's homepage

# Enter a URL: https://expired.badssl.com/
# SSL error occurred. Please check the URL and try again.

# Enter a URL: https://httpstat.us/404
# HTTP error occurred: 404 Client Error: Not Found for url: https://httpstat.us/404

# Enter a URL: https://httpstat.us/200?sleep=15000
# The request timed out. Please try again later.
