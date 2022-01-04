
import configparser
from datetime import datetime
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import crawl
import shutil
import lxml.html
from collections import OrderedDict

# From the crawlOutput for a URL return a Map of sheet name and dictionary
# Keys in the dictionary are the column values.
def extractData(website, url, crawlOutput):
    htmlDocument = lxml.html.fromstring(crawlOutput)
    fieldConfig = configparser.ConfigParser()
    fieldConfig.read('config/'+website+'/fields.properties')
    outputDictionary = OrderedDict()
    # Each Section is a sheet o/p excel
    for section in fieldConfig.sections():
        od = OrderedDict()
        od['url'] = url
        for (each_key, each_val) in fieldConfig.items(section):
            od[each_key] = htmlDocument.xpath(each_val)[0]
        outputDictionary[section] = od
    return outputDictionary






def initCrawl():
    commonConfig = configparser.ConfigParser()
    commonConfig.read('config/common.properties')
    outputDirectory = commonConfig.get("DEFAULT", "outputDirectory")
    websites = commonConfig.get("websites", "websitesToCrawl").split(",")
    for website in websites:

        print("Crawl initiated for " + website)
        currentDate = datetime.now().strftime("%m-%d-%Y")
        outputDirectory = outputDirectory + "/" +website + "/" +currentDate
        rows_list = []

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
                crawlOutput = crawl.Crawl.fetch(outputDirectory, url)
                if crawlOutput is not None:
                    print("Crawl Completed Successfully")
            # urlDict = extractData(website, url, crawlOutput)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initCrawl()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
