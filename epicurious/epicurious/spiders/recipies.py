import scrapy


class RecipiesSpider(scrapy.Spider):
    name = 'recipies'
    allowed_domains = ['www.epicurious.com/search?content=recipe']
    start_urls = ['https://www.epicurious.com/search?content=recipe']

    def parse(self, response):
        links = response.xpath("//article[@class='recipe-content-card']/a[2]/@href")
        for link in links:
            yield response.follow(link.get(), callback=self.parse_recipie, dont_filter=True)

    def parse_recipie(self, response):
        the_recipie = {}
        list_to_append_in_dictionary = []
        the_recipie['name'] = response.xpath("//h1[1]/text()").get()
        #here are 3 links contaning the divs of ingredientswhich have the same name class
        the_recipie["ingredients"] = response.xpath("//div[@class='List-XYTyX gPuEKn']/div[@class='BaseWrap-sc-TURhJ BaseText-fFzBQt Description-dSNklj eTiIvU eftAc']/text()").getall()
        #adding or appending each content from a div to key ingredient
        #for ingredients_of_recipie in ingredients:
        #    if "ingredients" in the_recipie:
        #        list_to_append_in_dictionary.append(response.xpath("normalize-space(.//div[@class='BaseWrap-sc-TURhJ BaseText-fFzBQt Description-dSNklj eTiIvU eftAc']/text())").get())
                
        #    else:
        #        list_to_append_in_dictionary.append(response.xpath("normalize-space(.//div[@class='BaseWrap-sc-TURhJ BaseText-fFzBQt Description-dSNklj eTiIvU eftAc']/text())").get()) 
        #        the_recipie["ingredients"] = list_to_append_in_dictionary

            
                
        yield the_recipie