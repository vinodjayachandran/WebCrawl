
import configparser
import json
from datetime import datetime
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import crawl
import shutil
from bs4 import BeautifulSoup


# From the crawlOutput for a URL return a Map of sheet name and dictionary
# Keys in the dictionary are the column values.
def extractData(website, url, crawlOutput):
    outputJson = {}
    outputJson['url'] = url
    # Opening JSON File
    f = open('config/' + website + '/fields.json')
    # returns JSON object as a dictionary
    data = json.load(f)
    for field in data :
        properties_dict = data[field]
        # Every Field is expected to have tagName and attributes key
        name = properties_dict['tagName']
        attributes = properties_dict['attributes']
        parsed_html = BeautifulSoup(crawlOutput, 'html.parser')
        field_value = parsed_html.body.find(name, attrs=attributes).text
        outputJson[field] = field_value
    print(outputJson)
    return outputJson


def writeToFile(fileName,content):
    file = open(fileName, 'w')
    file.write(content)
    file.close()
    print(f" File {fileName} written successfully")


def initCrawl():
    commonConfig = configparser.ConfigParser()
    commonConfig.read('config/common.properties')
    outputDirectory = commonConfig.get("DEFAULT", "outputDirectory")
    websites = commonConfig.get("websites", "websitesToCrawl").split(",")
    for website in websites:

        print("Crawl initiated for " + website)
        currentDate = datetime.now().strftime("%m-%d-%Y")
        outputDirectory = outputDirectory + "/" +website + "/" +currentDate
        print(f"Crawled HTML Pages for {website} will be placed at {outputDirectory}")
        shutil.rmtree(outputDirectory, ignore_errors=True)
        # Fetch URLs for the website
        urlFile = open('config/'+website+'/urls.txt', 'r')
        urls = urlFile.readlines()
        urlFile.close()
        urlSet = set()
        for url in urls:
            url = url.strip('\n')
            # Check if for duplicate URLs
            if(url not in urlSet):
                urlSet.add(url)
                fileName = url[url.rfind("/") + 1:len(url)]
                crawlOutput = crawl.Crawl.fetch(outputDirectory, url)
                scrapped_json = {}
                if crawlOutput is not None:
                    writeToFile(outputDirectory + "/" + fileName + ".html", crawlOutput)
                    scrapped_json = extractData(website,url,crawlOutput)
                    writeToFile(outputDirectory + "/" + fileName + ".json", json.dumps(scrapped_json))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initCrawl()


