from scrapy import Request
from scrapy import Selector
from scrapy.spiders import Spider

# Define class for ratings_247_Spider web scraper
class ratings_247_Spider(Spider):
  name = "sp1"
  start_urls = ["https://247sports.com/college/penn-state/Season/2018-Football/Commits/", "https://247sports.com/college/penn-state/Season/2017-Football/Commits/", "https://247sports.com/college/penn-state/Season/2016-Football/Commits/"]
  custom_settings = { 'DOWNLOAD_DELAY': 0.1, 'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
  
  # Def standard parse() function to parse the page
  def parse(self, response):
    # Get all list elements
    elements = response.xpath("//section[@class='ri-page__body']/div[@class='ri-page__main']/ul[@class='ri-page__list']/li[@class='ri-page__list-item']")
    items = []
	
    # Iterate through each top app 
    for element in elements:
      print("test")
      item = {}
	  
	  # Get elements
      item['name'] = element.xpath("./div[@class='recruit']/a[@class='ri-page__name-link']/text()").extract()
      item['page_url'] = element.xpath("./div[@class='recruit']/a[@class='ri-page__name-link']/@href").extract()
      item['rating'] = element.xpath("./div[@class='rating']/div[@class='ri-page__star-and-score']/span[@class='score']/text()").extract()
      item['position'] = element.xpath("./div[@class='position']/text()").extract()
      item['national_ranking'] = element.xpath("./div[@class='rating']/div[@class='rank']/a[@class='natrank']/text()").extract()
      item['position_ranking'] = element.xpath("./div[@class='rating']/div[@class='rank']/a[@class='posrank']/text()").extract()
      item['state_ranking'] = element.xpath("./div[@class='rating']/div[@class='rank']/a[@class='sttrank']/text()").extract()
      item['hometown_highschool_state'] = element.xpath(".//div[@class='recruit']/span[@class='meta']/text()").extract()
      item['early_enrollee'] = element.xpath("./div[@class='recruit']/span[@class='meta']").extract()
      item['height_weight'] = element.xpath("./div[@class='metrics']/text()").extract()
      item['commit_status_date'] = element.xpath("./div[@class='status']/p[@class='commit-date withDate']/text()").extract()
      item['image_url'] = element.xpath("./div[@class='circle-image-block']/img[@class='jsonly']/@src").extract()
	  
	  # TODO: Get class year from player subpage

      # Append the item
      items.append(item)

    return items