# 247_rating_scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

Update the parameters in the configuration file located at `./config/config.toml`. The toml file structure allows you to specify the spider name, user agent, download delay, and start URLs.

### 3. Run

Run the spider with the command: `scrapy crawl a247 -t csv -O data/output.csv`. Add other arguments as needed.