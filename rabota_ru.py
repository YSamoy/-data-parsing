import scrapy
from scrapy.http import HtmlResponse
from project_parser_hh.items import ProjectParserHhItem


class RabotaRuSpider(scrapy.Spider):
    name = 'rabota_ru'
    allowed_domains = ['rabota.ru']
    start_urls = ['https://nsk.rabota.ru/vacancy/?query=python&sort=relevance&period=three-days']


    def parse(self, response: HtmlResponse):
        for elements in self.start_urls:
          next_page =elements + '&'+ str(response.xpath('//a[@class="pagination-list__last-btn"]/@href').get())[2:]
          

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies =response.xpath('//a[@class="vacancy-preview-card__title_border"]/@href').getall()
        
        for url_vacancy in urls_vacancies:
            url_vacancy='https://nsk.rabota.ru'+str(url_vacancy)
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.xpath("//h1[@class='vacancy-card__title']/text()").get()
        vacancy_salary = response.xpath("//h3[@class='vacancy-card__salary']/text()").getall()
        vacancy_url = response.url
        
               

        yield ProjectParserHhItem(
            name=vacancy_name,
            salary=vacancy_salary,
            url=vacancy_url
        )
