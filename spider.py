import requests
import os

def google_search(api_key, cse_id, keyword, domain):
    # Define the endpoint and parameters
    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": keyword,
    }

    # Make the request
    response = requests.get(endpoint, params=params)
    results = response.json().get('items', [])

    # Check if the domain is in the search results
    found = False
    found_link = ""
    for result in results:
        link = result['link']
        if domain in link:
            print(f"Found {domain} in {link}")
            found = True
            found_link = link
            break
    if not found:
        print(f"{domain} not found in the first page of search results.")
    else:
        print(send_email(f"We have a new decision from the Ministry of Foreign Affairs, Egypt about Citizenship: {found_link}"))

def send_email(msg):
    print("Using " + os.environ["MAILGUN_API_KEY"])
    return requests.post(
  		"https://api.eu.mailgun.net/v3/fakharany.com/messages",
  		# auth=("api", os.environ["MAILGUN_API_KEY"]),
  		auth=("api", os.environ["MAILGUN_API_KEY"]),
  		data={"from": "Ahmed Elfakharany <mailgun@fakharany.com>",
  			"to": ["abohmeed@gmail.com"],
  			"subject": "New Ministry of Foreign Affairs descision",
  			"text": msg})

# Replace with your API key, CSE ID, keyword, and target domain
api_key = os.environ["GOOGLE_API_KEY"]
cse_id = os.environ["GOOGLE_CSE_ID"]
keyword = "الجريدة الرسمية تنشر قرار حصول"
domain = "youm7.com"

google_search(api_key, cse_id, keyword, domain)
