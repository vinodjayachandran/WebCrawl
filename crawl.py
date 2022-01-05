from pathlib import Path
from urllib.request import Request, urlopen

class Crawl:

    # Download the HTML Content of the URL and return absolute path of the HTML file
    @staticmethod
    def fetch(outputDirectory,url):
        try:
            # Create the output directory if not exists
            Path(outputDirectory).mkdir(parents=True, exist_ok=True)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req)
            #fileName = url[url.rfind("/")+1:len(url)]
            #htmlFile = open(outputDirectory + "/" +fileName+".html", 'w')
            htmlContent = response.read().decode("utf-8")
            #htmlFile.write(htmlContent)
            #htmlFile.close()
            #print(f"{url} crawled successfully and saved at {htmlFile.name}")
            return htmlContent
        except Exception as e:
            print(f'Crawl for {url} has failed' + str(e))
            errorFile = open(outputDirectory+"/failed.txt", 'a')
            errorFile.write(url+"\n")
            errorFile.close()

