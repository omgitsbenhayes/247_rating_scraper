# 247_rating_scraper
Scrapy based web-scraper for the 247 recruiting classes

## Usage

Follow the steps below to install, configure, and run the Scrapy spider.

### Installation

1. Download or clone the repository
2. Ensure ```python 3.6+``` and ```scrapy 2+``` are installed.

### Configuration

Update the parameters in the configuration file located at ```./config/config.toml```. The toml file structure allows you to specify the spider name, user agent, download delay, and start URLs.

### Run

Run the spider with the command: ```scrapy runspider ./python/247Sports_Team_Class_Scraper.py -t csv -O ./data/output.csv```