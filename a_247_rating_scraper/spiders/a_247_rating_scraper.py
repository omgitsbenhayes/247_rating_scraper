from scrapy import Request
from scrapy import Selector
from scrapy.spiders import Spider
from ..items import PlayerItem
from scrapy.loader import ItemLoader
from scrapy.item import Item, Field



# Define class for ratings_247_Spider web scraper
class ratings_247_Spider(Spider):
  name = "a247"
  start_urls = ["https://247sports.com/college/penn-state/Season/2022-Football/Commits/", 
                "https://247sports.com/college/penn-state/Season/2021-Football/Commits/",
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
                # "https://247sports.com/college/ohio-state/Season/2015-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2022-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2021-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2020-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2019-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2018-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2017-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2016-Football/Commits/",
                # "https://247sports.com/college/michigan/Season/2015-Football/Commits/",
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
      item = PlayerItem()
      l = ItemLoader(item=item, response=response)
	  
  	  # Get elements (using add_value() because it does not require creating a new ItemLoader for element)
      l.add_value('url', response.url)      
      l.add_value('sport', self._get_sport_from_url(response))
      l.add_value('name', element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/text()").extract())
      l.add_value('player_page_url', element.xpath(".//div[@class='recruit']/a[@class='ri-page__name-link']/@href").extract()[0])
      l.add_value('rating', element.xpath(".//div[@class='rating']/div[@class='ri-page__star-and-score']/span[@class='score']/text()").extract())
      l.add_value('national_ranking', element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='natrank']/text()").extract())
      l.add_value('position_ranking', element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='posrank']/text()").extract())
      l.add_value('state_ranking', element.xpath(".//div[@class='rating']/div[@class='rank']/a[@class='sttrank']/text()").extract())
      l.add_value('commit_status_date', element.xpath(".//div[@class='status']/p[@class='commit-date withDate']/text()").extract())

      yield Request("https:" + l.get_output_value('player_page_url')[0], callback=self.parse_commit, meta={'parent': l.load_item()})


  def parse_commit(self, response):
    # Assign item from parent
    item = response.meta['parent']

    # Create item loader
    l = ItemLoader(item=item, response=response)    

    # Determine if current commit (in current class) or former commit (in previous class)
    commit_status, url = self._determine_commit_status(response)

    # Handle current commits
    if commit_status:
      l.add_xpath('position', ".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Pos')]/following-sibling::span/text()")
      l.add_xpath('height', ".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Height')]/following-sibling::span/text()")
      l.add_xpath('weight', ".//div[@class='upper-cards']/ul[@class='metrics-list']//span[contains(text(), 'Weight')]/following-sibling::span/text()")
      l.add_xpath('home_town', ".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Home Town')]/following-sibling::span/text()")
      l.add_xpath('class_year', ".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'Class')]/following-sibling::span[1]/text()")
      l.add_xpath('team_name', ".//section[@class='main-content full']/section[@class='college-comp']/div/ul/li[span/text() = 'Committed' or span/text() = 'Signed' or span/text() = 'Enrolled']/div/a[@class='college-comp__team-name-link']/text()")
      l.add_xpath('high_school', ".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'High School')]/following-sibling::span//text()")
      # #item['high_school'] = response.xpath(".//div[@class='upper-cards']/ul[@class='details ']//span[contains(text(), 'High School')]/following-sibling::span/text()").extract()
      # # early enrollee
  
      l.add_value('early_enrollee', 1 if len(response.xpath(".//section[@class='main-content full']/header/div[@class='upper-cards']/ul[@class='details ']/li[span/text() = 'Class']/span[@class='icon-time']")) > 0 else 0)
      l.add_xpath('composite_rating', ".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/div/div[@class='rank-block']/text()")
      l.add_xpath('base_rating', ".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/div/div[@class='rank-block']/text()")

      comp_ratings = response.xpath(".//section[@class='main-wrapper']//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section' and h3[contains(text(), '247Sports Com')]]//ul[@class='ranks-list']/li")
      for rating in comp_ratings:
        if 'comp_' + rating.xpath(".//b/text()").get() in item.fields:
          l.add_value('comp_' + rating.xpath(".//b/text()").get(), rating.xpath(".//strong/text()").get())
        else:
          item.fields['comp_' + rating.xpath(".//b/text()").get()] = Field()
          l.add_value('comp_' + rating.xpath(".//b/text()").get(), rating.xpath(".//strong/text()").get())

      base_ratings = response.xpath(".//section[@class='main-wrapper']//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section' and h3[text() = '247Sports']]//ul[@class='ranks-list']/li")
      for rating in base_ratings:
        if 'base_' + rating.xpath(".//b/text()").get() in item.fields:
          l.add_value('base_' + rating.xpath(".//b/text()").get(), rating.xpath(".//strong/text()").get())        
        else:
          item.fields['base_' + rating.xpath(".//b/text()").get()] = Field()
          l.add_value('base_' + rating.xpath(".//b/text()").get(), rating.xpath(".//strong/text()").get())        
      
      #item['composite_natl_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[1]/b/following-sibling::a/strong/text()").extract()
      #item['composite_pos_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[2]/b/following-sibling::a/strong/text()").extract()
      #item['composite_state_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][1]/ul[@class='ranks-list']/li[3]/b/following-sibling::a/strong/text()").extract()
      #item['base_natl_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[1]/b/following-sibling::a/strong/text()").extract()
      #item['base_pos_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[2]/b/following-sibling::a/strong/text()").extract()
      #item['base_state_rank'] = response.xpath(".//div[@class='lower-cards']/section[@class='rankings']/section[@class='rankings-section'][2]/ul[@class='ranks-list']/li[3]/b/following-sibling::a/strong/text()").extract()
      
      l.add_xpath('player_num_offers', ".//section[@class='college-comp']/header/div/span[1]/text()")
      l.add_xpath('player_num_visits', ".//section[@class='college-comp']/header/div/span[2]/text()")
      l.add_xpath('player_num_coachvisits', ".//section[@class='college-comp']/header/div/span[3]/text()")      
      l.add_value('commit_list_url', response.xpath(".//footer[@class='college-comp__footer']/a[@class='college-comp__view-all']/@href").extract()[0])
      
      # Call REQUEST (parse_offers)
      yield Request(l.get_output_value('commit_list_url')[0], callback=self.parse_offers, meta={'commit': l.load_item()})
  
    else:
      # Call REQUEST (parse_commit)
      yield Request(url, callback=self.parse_commit, meta={'parent': item})


  def parse_offers(self, response):
    # Assign item from parent meta
    item = response.meta['commit']

    # Count number of team list offers
    item['teamlist_num_offers'] = len(response.xpath(".//section//div[@class='secondary_blk']/span[contains(., 'Yes')]").extract())

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