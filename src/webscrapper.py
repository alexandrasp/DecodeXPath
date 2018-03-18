from lxml import html
import requests

response = requests.get('https://s3-eu-west-1.amazonaws.com/legalstart/thumbscraper_input_tampered.hiring-env.json')

data = response.json()

#test=html.xpath(data['0']['xpath_test_query'])

print(data['0']['xpath_test_query'])