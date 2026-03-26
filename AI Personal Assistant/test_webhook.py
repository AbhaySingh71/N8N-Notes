import requests


user_message = "Can you tell me about black holes in 3-4 lines?"

request_message = {"message": user_message}

url = "https://abhay71.app.n8n.cloud/webhook-test/83459fbf-c9dd-41f4-b533-1cc849393e1e"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json())
#print(response.json()[0]["output"])