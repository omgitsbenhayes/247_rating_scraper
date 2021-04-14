# 247_rating_scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/omgitsbenhayes/247_rating_scraper/issues)


Multi-page `Scrapy-based web-scraper` for 247 recruiting classes. Pulls values like name, home town, high school, ratings, position, etc (for a full list view the details below). The tool currently focuses primarily on football but may work with some basketball team pages. Built entirely using `python`.

> Note: This repository is for demonstration and educational purposes only. 
> Web-scraping is a fast-evolving, exciting field and the potential of tools 
> like Scrapy are shown here.


## Usage

Follow the steps below to install, configure, and run the Scrapy spider. The spider will process each of the start URLs and navigate to the player detail pages. See the note above for more information on when to use this code.

### 1. Installation

1. Download or clone the repository
2. Ensure `python 3.6+` and `scrapy 2+` and any other dependencies are installed.

### 2. Configuration

Update the parameters in the settings file located at `./a_247_rating_scraper/settings.py`. `START_URLS` should be declared in the main spider file itself `./a_247_rating_scraper/a_247_rating_scraper.py`.

### 3. Run

* To get a JSON file (recommended): Run the spider with the command: `scrapy crawl a247 -t json -O data/output.json`. Add other arguments as needed.
* To get a CSV file: Run the spider with the command: `scrapy crawl a247 -t csv -O data/output.csv`. Add other arguments as needed. Note that columns may be missing headings while using CSV files due to the way Scrapy writes CSV files and determines headings [see more here](https://docs.scrapy.org/en/latest/_modules/scrapy/exporters.html#CsvItemExporter).


## Data Fields

### Team Page Details

* Team page URL
* Sport
* Recruit name
* Rating (e.g., 0.9500)
* National ranking (e.g., #214)
* Position ranking (e.g., #13)
* State ranking (e.g., #6)
* Commit status/date
* Recruit page URL --> (scraped for recruit details)

### Recruit Page Details

#### Recruit Background Info

* Position (e.g., WR)
* Height
* Weight
* Hometown
* Class year (e.g., 2020)
* Team name (e.g., Penn State)
* High school
* Early enrollee (e.g., 1 if early enrollee)
* Composite rating (should match Rating afrom team page details, e.g., 0.9500)
* Base rating (e.g., 0.9450)
* National ranking (composite)
* Position ranking (composite)
* State ranking (composite)
* National ranking (base)
* Position ranking (base)
* State ranking (base)

#### Recruit Evaluation Info

* Evaluation date
* Evaluation evaluator name
* Evaluation projection (round, day)
* Evaluation comparison (e.g., Bud Dupree)
* Evaluation text (e.g., Alex Alexson is an elite athlete with top level talent. Clearly deserving of his 0.9500 rating)
* Athletic background (e.g., Alex Alexson is a 6-1 WR from south Texas)

#### Recruit Commitment Info

* Number of offers received (e.g., 24)
* Number of visits (e.g., 2)
* Number of coaching visits (e.g., 1)
* Commit list URL --> (scraped for full commitment page details)

### Commitment Page Details

* Number of offers received (should match value above from recruit page)
* Schools that offered recruit (e.g., Alabama --> Yes if Alabama offered recruit)
