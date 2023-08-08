import requests as rq

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=890603a55bfa47048e4490069ebee18c"

# Make request
get_info = rq.get(url)

# Get Dictionary with data
content = get_info.json()

# Access article titles & description
for article in content["articles"]:
      print(article["title"])
      print(article["description"] + '\n')
