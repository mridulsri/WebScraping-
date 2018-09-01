# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
import csv
import time

class SampleSpider(Spider):
    name = 'sample'
    allowed_domains = ['cookcountyassessor.com']
    start_urls = ['http://cookcountyassessor.com/']

    def parse(self, response):
        try:
            with open('D:\\Test_Inputs.csv') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                data = []
                for row in reader:
                    try:
                        data.append(row)
                        if row[1].strip() == 'nan':
                            continue
                        url = 'http://cookcountyassessor.com/Property.aspx?mode=details&pin=' + row[1].strip()
                        print(url)
                        # time.sleep(2)
                        yield scrapy.Request(url, callback=self.parse_items)
                    except Exception as e:
                        print(e)
        except Exception as ex:
            print(ex)

    def parse_items(self, response):
        item = {}
        try:
            item['APN'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoPIN"]/text()').extract_first(default='N/A')
            item['Situs Street'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoAddress"]/text()').extract_first(default='N/A')
            item['Situs City'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoCity"]/text()').extract_first(default='N/A')
            item['Situs State'] = 'IL'
            item['Situs County Name'] = 'Cook'
            item['Land Use Code'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoClassification"]/text()').extract_first(default='N/A')
            item['Landuse Designation'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharDesc"]/text()').extract_first(default='N/A')
            item['Legal Description'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharDesc"]/text()').extract_first(default='N/A')
            item['Property Type'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharUse"]/text()').extract_first(default='N/A')
            item['Exterior Construction'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharExtConst"]/text()').extract_first(default='N/A')
            item['# of Units'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharApts"]/text()').extract_first(default='N/A')

            item['Age'] = response.xpath(
                '//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharAge"]/text()').extract_first(default='N/A')
            item['Year Built'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharAge"]/text()').extract_first(default='N/A')

            item['Lot Size'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoSqFt"]/text()').extract_first(default='N/A')
            item['Square Feet'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharBldgSqFt"]/text()').extract_first(default='N/A')
            item['Finished Basement Area'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharBasement"]/text()').extract_first(default='N/A')
            item['Garage Area'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharGarage"]/text()').extract_first(default='N/A')
            item['Bedroom'] = 'Not Clear on page' # response.xpath('').extract_first()
            item['Bath'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharFullBaths"]/text()').extract_first(default='N/A')
            item['Heating/Cooling'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharCentAir"]/text()').extract_first(default='N/A')
            item['Fireplaces'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropCharFrpl"]/text()').extract_first(default='N/A')
            item['Tax Rate Area'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblPropInfoTaxcode"]/text()').extract_first(default='N/A')

            item['Base Year'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblAsdValCurYear"]/text()').extract_first(default='N/A')
            item['Land Value'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblAsdValLandFirstPass"]/text()').extract_first(default='N/A')
            item['Structure Value'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblAsdValBldgFirstPass"]/text()').extract_first(default='N/A')
            item['Personal Property Value'] = 'Not Clear on page' # response.xpath('').extract_first()
            item['Net Assessed Value'] = response.xpath('//*[@id="ctl00_phArticle_ctlPropertyDetails_lblAsdValTotalFirstPass"]/text()').extract_first(default='N/A')

            yield item
        except Exception as ex:
            print(ex)


