from scrapy import Request
from scrapy import Selector
from scrapy.spiders import Spider
# from ..items import PlayerItem
# from scrapy.loader import ItemLoader
# from scrapy.item import Item, Field



# Define class for ratings_247_Spider web scraper
class ratings_247_Spider(Spider):
  name = "a247"
  start_urls = ["https://247sports.com/college/penn-state/Season/2022-Football/Commits/", 
                "https://247sports.com/college/penn-state/Season/2021-Football/Commits/",
                "https://247sports.com/college/penn-state/Season/2020-Football/Commits/",
                "https://247sports.com/college/penn-state/Season/2019-Football/Commits/",
                "https://247sports.com/college/penn-state/Season/2018-Football/Commits/", 
                "https://247sports.com/college/penn-state/Season/2017-Football/Commits/", 
                "https://247sports.com/college/penn-state/Season/2016-Football/Commits/",
                # "https://247sports.com/college/penn-state/Season/2015-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2022-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2021-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2020-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2019-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2018-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2017-Football/Commits/",
                "https://247sports.com/college/ohio-state/Season/2016-Football/Commits/",
                # "https://247sports.com/college/ohio-state/Season/2015-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2022-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2021-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2020-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2019-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2018-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2017-Football/Commits/",
                "https://247sports.com/college/michigan/Season/2016-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2015-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2022-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2021-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2020-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2019-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2018-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2017-Football/Commits/",
                "https://247sports.com/college/alabama/Season/2016-Football/Commits/",
                # "https://247sports.com/college/alabama/Season/2015-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2022-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2021-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2020-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2019-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2018-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2017-Football/Commits/",
                "https://247sports.com/college/georgia/Season/2016-Football/Commits/",
                # "https://247sports.com/college/georgia/Season/2015-Football/Commits/", 
                "https://247sports.com/college/oklahoma/Season/2022-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2021-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2020-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2019-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2018-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2017-Football/Commits/",
                "https://247sports.com/college/oklahoma/Season/2016-Football/Commits/",
                # "https://247sports.com/college/oklahoma/Season/2015-Football/Commits/", 
                "https://247sports.com/college/texas/Season/2022-Football/Commits/",
                "https://247sports.com/college/texas/Season/2021-Football/Commits/",
                "https://247sports.com/college/texas/Season/2020-Football/Commits/",
                "https://247sports.com/college/texas/Season/2019-Football/Commits/",
                "https://247sports.com/college/texas/Season/2018-Football/Commits/",
                "https://247sports.com/college/texas/Season/2017-Football/Commits/",
                "https://247sports.com/college/texas/Season/2016-Football/Commits/",
                # "https://247sports.com/college/texas/Season/2015-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2022-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2021-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2020-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2019-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2018-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2017-Football/Commits/",
                "https://247sports.com/college/clemson/Season/2016-Football/Commits/",
                # "https://247sports.com/college/clemson/Season/2015-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2022-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2021-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2020-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2019-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2018-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2017-Football/Commits/",
                "https://247sports.com/college/lsu/Season/2016-Football/Commits/",
                # "https://247sports.com/college/lsu/Season/2015-Football/Commits/",
                #"https://247sports.com/college/penn-state/Season/2020-Basketball/Commits/",
                ]
  

  ###################
  # Parse functions #
  ###################

  # Def standard parse() function to parse the page
  def parse(self, response):
    # Get all list elements
    elements = response.xpath("//section[@class='ri-page__body']/div[@class='ri-page__main']/ul[@class='ri-page__list']/li[@class='ri-page__list-item']")

    # Iterate through each player 
    for element in elements:
      item = {}
	  
  	  # Get elements (using add_value() because it does not require creating a new ItemLoader for element)
      item['url'] = response.url
      item['sport'] = self._get_sport_from_url(response)
      item['name'] = element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/text()").extract()
      item['player_page_url'] = element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/@href").extract()[0]
      item['rating'] = element.xpath(".//div[@class='rating']/div[@class='ri-page__star-and-score']/span[@class='score']/text()").extract()
      item['national_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='natrank']/text()").extract()
      item['position_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='posrank']/text()").extract()
      item['state_ranking'] = element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='sttrank']/text()").extract()
      item['commit_status_date'] = element.xpath(".//div[@class='status']/p[@class='commit-date withDate']/text()").extract()

      yield Request("https:" + item['player_page_url'], callback=self.parse_commit, meta={'parent': item})


  def parse_commit(self, response):
    # Assign item from parent
    item = response.meta['parent']

    # Determine if current commit (in current class) or former commit (in previous class)
    commit_status, url = self._determine_commit_status(response)

    # Handle current commits
    if commit_status:
      item['position'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Pos')]/following-sibling::span/text()").get()
      item['height'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Height')]/following-sibling::span/text()").get()
      item['weight'] = response.xpath(".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Weight')]/following-sibling::span/text()").get()
      item['home_town'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Home Town')]/following-sibling::span/text()").get()
      item['class_year'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Class')]/following-sibling::span[1]/text()").get()
      item['team_name'] = response.xpath(".//section[@class='main-content full']/section[@class='college-comp']/div/ul/li[span/text() = 'Committed' or span/text() = 'Signed' or span/text() = 'Enrolled']/div/a[@class='college-comp__team-name-link']/text()").get()
      item['high_school'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'High School')]/following-sibling::span//text()").get()
      item['early_enrollee'] = 1 if len(response.xpath(".//section[@class='main-content full']/header/div[@class='upper-cards']/ul[@class='details ']/li[span/text() = 'Class']/span[@class='icon-time']")) > 0 else 0
      item['composite_ranking'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/div/div[@class='rank-block']/text()").get()
      item['base_rating'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/div/div[@class='rank-block']/text()").get()

      comp_ratings = response.xpath(".//section[@class='main-wrapper']//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section' and h3[contains(text(), '247Sports Com')]]//ul[@class='ranks-list']/li")
      for rating in comp_ratings:
        item['comp_' + rating.xpath(".//b/text()").get()] = rating.xpath(".//strong/text()").get()

      base_ratings = response.xpath(".//section[@class='main-wrapper']//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section' and h3[text() = '247Sports']]//ul[@class='ranks-list']/li")
      for rating in base_ratings:
        item['base_' + rating.xpath(".//b/text()").get()] = rating.xpath(".//strong/text()").get()

      item['player_num_offers'] = response.xpath(".//section[@class='college-comp']/header/div/span[1]/text()").get()
      item['player_num_visits'] = response.xpath(".//section[@class='college-comp']/header/div/span[2]/text()").get()
      item['player_num_coachvisits'] = response.xpath(".//section[@class='college-comp']/header/div/span[3]/text()").get()
      item['commit_list_url'] = response.xpath(".//footer[@class='college-comp__footer']/a[@class='college-comp__view-all']/@href").extract()[0]

      # Call REQUEST (parse_offers)
      yield Request(item['commit_list_url'] , callback=self.parse_offers, meta={'commit': item})
  
    else:
      # Call REQUEST (parse_commit)
      yield Request(url, callback=self.parse_commit, meta={'parent': item})


  def parse_offers(self, response):
    # Assign item from parent meta
    item = response.meta['commit']

    # Count number of team list offers
    item['teamlist_num_offers'] = len(response.xpath(".//section//div[@class='secondary_blk']/span[contains(., 'Yes')]").extract())

    # Get school offers by program
    school_offers = response.xpath(".//section[@class='list-body']/section/ul/li//div[div[@class='first_blk'] and //span[@class='offer' and text()[contains(., 'Yes')]]]/div[@class='first_blk']/a[1]")
    for school in school_offers:
      item['offer' + school.xpath('./text()').get()] = "Y"

    yield item


  ####################
  # Helper functions #
  ####################

  def _get_sport_from_url(self, response):
      _, _, _, _, _, _, a, _, _ = response.url.split('/')
      return a[5:]

  def _determine_commit_status(self, response):
    current, url = True, ""
    recruit_link = response.xpath(".//section[@class='main-content full']//a[@class='view-profile-link']/@href")

    if len(recruit_link) > 0:
      url = recruit_link.extract()[0]
      current = False
      
    return current, url