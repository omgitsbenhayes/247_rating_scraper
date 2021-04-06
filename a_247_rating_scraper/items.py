# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PlayerItem(Item):

    url = Field()
    sport = Field()
    name = Field()
    player_page_url = Field()
    rating = Field()
    position = Field()
    national_ranking = Field()
    position_ranking = Field()
    state_ranking = Field()
    commit_status_date = Field()
    high_school = Field()
    early_enrollee = Field()
    team_name = Field()
    position = Field()
    height = Field()
    weight = Field()
    home_town = Field()
    class_year = Field()
    composite_rating = Field()
    base_rating = Field()
    player_num_offers = Field()
    player_num_visits = Field()
    player_num_coachvisits = Field()
    commit_list_url = Field()
    teamlist_num_offers = Field()
    row = Field()