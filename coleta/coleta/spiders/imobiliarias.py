import scrapy


class ImobiliariasSpider(scrapy.Spider):
    name = "imobiliarias"
    allowed_domains = ["daterraimoveis.com.br"]
    start_urls = ["https://daterraimoveis.com.br/imoveis/para-alugar"]

    def parse(self, response):
        pass
