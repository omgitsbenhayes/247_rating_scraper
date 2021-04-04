from scrapy import Request
from scrapy import Selector
from scrapy.spiders import Spider

# Define class for ratings_247_Spider web scraper
class ratings_247_Spider(Spider):
  name = "sp1"
  start_urls = ["https://247sports.com/college/penn-state/Season/2022-Football/Commits/", 
                #"https://247sports.com/college/penn-state/Season/2021-Football/Commits/",
                #"https://247sports.com/college/penn-state/Season/2020-Basketball/Commits/",
                # "https://247sports.com/college/penn-state/Season/2020-Football/Commits/",
                # "https://247sports.com/college/penn-state/Season/2019-Football/Commits/",
                # "https://247sports.com/college/penn-state/Season/2018-Football/Commits/", 
                # "https://247sports.com/college/penn-state/Season/2017-Football/Commits/", 
                # "https://247sports.com/college/penn-state/Season/2016-Football/Commits/",
                # "https://247sports.com/college/penn-state/Season/2015-Football/Commits/",
                #"https://247sports.com/college/ohio-state/Season/2022-Football/Commits/",
                #"https://247sports.com/college/ohio-state/Season/2021-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2020-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2019-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2018-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2017-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2016-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2015-Football/Commits/"
                ]
  custom_settings = { 'DOWNLOAD_DELAY': 0.135, 'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
  
  # Def standard parse() function to parse the page
  def parse(self, response):
    # Get all list elements
    elements = response.xpath("//section[@class='ri-page__body']/div[@class='ri-page__main']/ul[@class='ri-page__list']/li[@class='ri-page__list-item']")
    items = []
	
    # Iterate through each top app 
    for element in elements:
      item = {}
	  
	  # Get elements
      item['name'] = element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/text()").extract()
      item['page_url'] = element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/@href").extract()[0]
      item['rating'] = element.xpath(".//div[@class='rating']/div[@class='ri-page__star-and-score']/span[@class='score']/text()").extract()
      item['position'] = element.xpath(".//div[@class='position']/text()").extract()
      item['national_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='natrank']/text()").extract()
      item['position_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='posrank']/text()").extract()
      item['state_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='sttrank']/text()").extract()
      #item['hometown_highschool_state'] = element.xpath(".//div[@class='recruit']/span[@class='meta']/text()").extract()
      #item['early_enrollee'] = element.xpath(".//div[@class='recruit']/span[@class='meta']").extract()
      #item['height'], item['weight'] = element.xpath(".//div[@class='metrics']/text()").extract()[0].split('/')
      item['commit_status_date'] = element.xpath(".//div[@class='status']/p[@class='commit-date withDate']/text()").extract()
      #item['image_url'] = element.xpath(".//div[@class='circle-image-block']/img[@class='jsonly']/@src").extract()

      yield Request("https:" + item['page_url'], callback=self.parse_commit, meta={'parent': item})


  def parse_commit(self, response):
    parent_item = response.meta['parent']
    commit_status, url = self._determine_commit_status(response)

    # Handle current commits
    if commit_status:
      parent_item['position'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Pos')]/following-sibling::span/text()").extract()    
      parent_item['height'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Height')]/following-sibling::span/text()").extract()
      parent_item['weight'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Weight')]/following-sibling::span/text()").extract()
      #parent_item['high_school'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'High School')]/following-sibling::span/text()").extract()
      #parent_item['high_school'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'High School')]//text()").extract()
      parent_item['home_town'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Home Town')]/following-sibling::span/text()").extract()
      parent_item['class'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Class')]/following-sibling::span[1]/text()").extract()
      # early enrollee
  
      parent_item['composite_rating'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/div/div[@class='rank-block']/text()").extract()
      parent_item['base_rating'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/div/div[@class='rank-block']/text()").extract()
      

      parent_item['test'] = response.xpath(".//section[@class='main-wrapper']//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section' and contains(h3.text(), '247Sports Com')]").extract()

      # for ___ in ___:
      #   parent_item['comp_' + ___] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section']/descendant").extract()

      # for ___ in ___:
      #   parent_item['base_' + ___]
      
      #parent_item['composite_natl_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[1]/b/following-sibling::a/strong/text()").extract()
      #parent_item['composite_pos_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[2]/b/following-sibling::a/strong/text()").extract()
      #parent_item['composite_state_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[3]/b/following-sibling::a/strong/text()").extract()
      #parent_item['base_natl_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[1]/b/following-sibling::a/strong/text()").extract()
      #parent_item['base_pos_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[2]/b/following-sibling::a/strong/text()").extract()
      #parent_item['base_state_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[3]/b/following-sibling::a/strong/text()").extract()
      parent_item['player_num_offers'] = response.xpath(".//section[@class='college-comp']/header/div/span[1]/text()").extract()
      parent_item['player_num_visits'] = response.xpath(".//section[@class='college-comp']/header/div/span[2]/text()").extract()
      parent_item['player_num_coachvisits'] = response.xpath(".//section[@class='college-comp']/header/div/span[3]/text()").extract()
      parent_item['commit_list_url'] = response.xpath(".//footer[@class='college-comp__footer']/a[@class='college-comp__view-all']/@href").extract()[0]
      
      # Call REQUEST (parse_offers)
      yield Request(parent_item['commit_list_url'], callback=self.parse_offers, meta={'commit': parent_item})
  
    else:
      # Call REQUEST (parse_commit)
      yield Request(url, callback=self.parse_commit, meta={'parent': parent_item})


  def parse_offers(self, response):
    commit_item = response.meta['commit']
    commit_item['teamlist_num_offers'] = len(response.xpath(".//section//div[@class='secondary_blk']/span[contains(., 'Yes')]").extract())
    

    yield commit_item


  def _determine_commit_status(self, response):
    current, url = True, ""
    recruit_link = response.xpath(".//section[@class='main-content full']//a[@class='view-profile-link']/@href")

    if len(recruit_link) > 0:
      url = recruit_link.extract()[0]
      current = False
      
    return current, url