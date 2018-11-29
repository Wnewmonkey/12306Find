from Station_Code import Stations
import json
import urllib.request

class HtmlDownloader(object):
    """获取data"""
    def getData(self,url):

        data = ''
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return data
    def download(self,info):
        a = Stations().stations[info['from_station']]
        b = Stations().stations[info['to_station']]
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT'.format(
            info['from_date'], a, b)

        while 1:
            try:
                data = self.getData(url)
                lists = json.loads(data)["data"]["result"]
                return lists
                break
            except:
                continue
