# WebScraper : Scrape CNBC and Forbes news
#### -- Project Status: [Completed]

## Project Intro/Objective
爬取美國財經新聞網站CNBC以及Forbes歷史新聞資料
利用關鍵字搜尋，輸入欲爬取相關新聞之關鍵字，可爬取所有與此關鍵字相關的新聞標題與內容。

### Library
* Scrapy
* requests
* Beautifulsoup

### Step by Step
1. 啟動專案將可用的free proxy載下來整理成json file.
2. 在spiders/reuters.py中修改欲下載的關鍵字以及新聞網址
3. 啟動專案reuters專案可開始下載
