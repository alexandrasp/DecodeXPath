import lxml.html
import yaml
from lxml import etree
import requests

config = yaml.load(open('/Users/apereira/Downloads/TesteHekima/Legal/src/systemConfig.yaml'))
responseJson = requests.get(config['json_info']['input_json'])
jsonData = responseJson.json()
urlBase = config['url_info']['base_url']
user = config['credentials']['user']
password = config['credentials']['password']

def getHtmlFile(url_name, user, password):
    htmlFile = requests.get(url_name, auth=(user, password)) 
    return htmlFile

for i in range(len(jsonData)):
    if i == 0:
        nextPage = jsonData[str(i)]['next_page_expected']
        responseHtml = getHtmlFile(urlBase, user, password)
        htmlText = lxml.html.fromstring(responseHtml.content)
        parsedContent = htmlText.xpath(jsonData[str(i)]['xpath_test_query'])
        nextLink = htmlText.xpath(jsonData[str(i)]['xpath_button_to_click'])
        if validParser(parsedContent, jsonData[str(i)]['xpath_test_result']):
            print(outputMessage(True, i))
        else:
            print(outputMessage(False, i))
    else:
        responseHtml = getHtmlFile(urlBase+nextLink[0].get('href'), user, password)
        htmlText = lxml.html.fromstring(responseHtml.content)
        parsedContent = htmlText.xpath(jsonData[str(nextPage)]['xpath_test_query'])
        nextLink = htmlText.xpath(jsonData[str(nextPage)]['xpath_button_to_click'])
        if validParser(parsedContent, jsonData[str(nextPage)]['xpath_test_result']):
            print(outputMessage(True, i))
        else:
            print(outputMessage(False, i))
        nextPage = jsonData[str(nextPage)]['next_page_expected']
