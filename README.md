# 247_rating_scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)


Multi-page `Scrapy-based web-scraper` for 247 recruiting classes. Pulls values like name, home town, high school, ratings, position, etc. The tool currently focuses primarily on football but may work with some basketball team pages. Built entirely using `python`.

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
* To get a CSV file: Run the spider with the command: `scrapy crawl a247 -t csv -O data/output.csv`. Add other arguments as needed. Note that columns may be missing headings while using CSV files.
