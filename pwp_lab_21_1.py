# Building a Simple API Client (Write a simple Python class that encapsulates the functionality for making GET and POST requests to the JSONPlaceholder API. Include methods for fetching posts and creating a new post.)

import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def get_posts(self):
        """Fetch all posts"""
        url = f"{self.BASE_URL}/posts"
        response = self.session.get(url)
        return response.json()

    def get_post(self, post_id):
        """Fetch a single post by ID"""
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.get(url)
        return response.json()

    def create_post(self, title, body, user_id):
        """Create a new post"""
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = self.session.post(url, json=payload)
        return response.json()

# Example:
if (__name__ == "__main__"):
    client = JSONPlaceholderClient()
        
    print ("Fetching Request")
    posts = client.get_posts()
    print (posts[:2]) # print first 2 posts
        
    print ("\nFetching post 1")
    print (client.get_post(1))
        
    print ("\nCreating a new post")
    result = client.create_post ("This is the Title", "This is my post", 1)
    print (result)