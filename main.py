import requests
from lxml import etree
from pymongo import MongoClient

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


client = MongoClient('127.0.0.1', 27017)
db = client['youshang']
col = db['apple']


def screen():
    r = requests.get('https://support.apple.com/es-es/iphone/repair/service/screen-replacement', headers=headers)
    html = etree.HTML(r.text)
    nodes = html.xpath('//*[@id="tableWraper"]/table/tbody/tr')[1:]
    if nodes:
        for node in nodes:
            iphone_type = ''.join(node.xpath('./td[1]//text()')).split(',')
            for i_type in iphone_type:
                item = {}
                item['品牌'] = 'APPLE'
                item['产品类型'] = '手机'
                item['传播名'] = i_type.strip()
                item['物料类型'] = 'screen'
                item['保内价格'] = ''.join(node.xpath('./td[2]//text()')).replace('\xa0', ' ')
                item['保外价格'] = ''.join(node.xpath('./td[3]//text()'))
                item['人工费'] = ''
                item['价格备注'] = '这些超出保修期的价格仅适用于Apple进行的维修。Apple授权服务提供商可能会提供不同的价格。所有价格均为欧元，包括增值税。保修期外的价格包括12.10欧元的运输费，只有在必须发送iPhone的情况下，我们才会收取该费用。意外损坏不在Apple的保修范围之内。如果屏幕由于制造缺陷而出现故障，则可能受到Apple的保修，AppleCare +计划或消费者保护法的保护。'
                item['网址'] = 'https://support.apple.com/es-es/iphone/repair/service/screen-replacement'
                print(item)
                col.insert(item)
                col.insert_one(item)


def battery():
    r = requests.get('https://support.apple.com/es-es/iphone/repair/service/battery-power', headers=headers)
    html = etree.HTML(r.text)
    nodes = html.xpath('//*[@id="tableWraper"]/table/tbody/tr')[1:]
    if nodes:
        for node in nodes:
            iphone_type = ''.join(node.xpath('./td[1]//text()')).split(',')
            for i_type in iphone_type:
                item = {}
                item['品牌'] = 'APPLE'
                item['产品类型'] = '手机'
                item['传播名'] = i_type.strip().replace('\xa0', ' ')
                item['物料类型'] = 'battery'
                item['保内价格'] = ''.join(node.xpath('./td[2]//text()')).replace('\xa0', ' ')
                item['保外价格'] = ''.join(node.xpath('./td[3]//text()')).replace('\xa0', '')
                item['人工费'] = ''
                item[
                    '价格备注'] = '这些价格仅适用于Apple进行的电池维修。授权的Apple服务提供商提供的价格可能有所不同。如果需要维修以发送iPhone且不在保修范围内，则我们将增加€12.10的运输费用。所有价格均为欧元，包括增值税。'
                item['网址'] = 'https://support.apple.com/es-es/iphone/repair/service/battery-power'
                print(item)
                col.insert(item)


if __name__ == '__main__':
    screen()
    battery()