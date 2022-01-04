# WebCrawl
Crawls a list of URLs and provide HTML content

### Limitations
1. Doesn't Crawl pages which needs user login
2. Doesn't have mechanisms to over come site blocking

### Usage
1. Configure the websites to be crawled in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties) file websitesToCrawl property.
2. Create a folder under config for each website mentioned in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties) file websitesToCrawl property.
3. Specify the URLs to be crawled (one per line) in urls.txt under the corresponding website folder in [config](https://github.com/vinodjayachandran/WebCrawl/tree/main/config)
4. [OPTIONAL] Change the directory where the HTML content needs to be placed in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties) file outputDirectory property
5. Run main.py
