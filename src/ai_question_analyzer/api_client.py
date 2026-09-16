import requests

def fetch_todo():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout = 5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def send_question(question):
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": question
    }
    try:
        response = requests.post(url, json=data, timeout = 5)
        if response.status_code == 201:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
    
