import lxml.html
import yaml
import os
from lxml import etree
import requests

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'systemConfig_sample.yaml')
config = yaml.load(open(config_file))
responseJson = requests.get(config['json_info']['input_json'])
jsonData = responseJson.json()
urlBase = config['url_info']['base_url']
user = config['credentials']['user']
password = config['credentials']['password']

def getHtmlFile(url_name, user, password):
    htmlFile = requests.get(url_name, auth=(user, password)) 
    return htmlFile

def validParser(parsedContent, result):
    if parsedContent == result:
        return True
    else:
        return False

def outputMessage(boolean, step):    
    if boolean:
        return "Move to page "+str(step+1)
    else:
        return "ALERT - Can’t move to page "+str(step+1)+": page "+str(step)+" link has been malevolently tampered with!!"

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
