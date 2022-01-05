# WebCrawl
Crawls multiple URLs -> Download their HTML content -> Extract info and save it as JSON


### Limitations
1. Doesn't Crawl pages which needs user login
2. Doesn't have mechanisms to over come site blocking

### Usage
1. Configure the websites to be crawled in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties) file websitesToCrawl property.
2. Create a folder under config for each website mentioned in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties) file websitesToCrawl property.
3. Specify the URLs to be crawled (one per line) in urls.txt under the corresponding website folder in [config](https://github.com/vinodjayachandran/WebCrawl/tree/main/config)
4. [OPTIONAL] Change the outputDirectory property in [common.properties](https://github.com/vinodjayachandran/WebCrawl/blob/main/config/common.properties).  outputDirectory will contain the HTML pages and extracted values as json for each url under {outputDirectory}/{website}/{mm-dd-yyyy}
5. Specify the fields to be extracted in fields.json under the corresponding website folder in [config](https://github.com/vinodjayachandran/WebCrawl/tree/main/config). Refer to existing fields json structure for configuring new fields
6. Run main.py


### To Dos
1. [ ] Add json schema and validation for fields.json under the corresponding website folder in [config](https://github.com/vinodjayachandran/WebCrawl/tree/main/config)
2. [ ] Add capability to have outputDirectory on cloud,  For example AWS S3
3. [ ] Add capability to run the script from serverless architecture such as AWS lambda


> PRs for above To Dos and new ideas are welcome :smiley:
