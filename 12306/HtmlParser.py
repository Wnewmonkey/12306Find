import json

import color as color

from Station_Code import Stations
from prettytable import PrettyTable
from HtmlDownloader import HtmlDownloader
class HtmlParser(object):
    def __init__(self):
        self.download = HtmlDownloader()
    def price_url(self,items):
        price_data = {
            "train_no":'',
            "from_station_no":'',
            "to_station_no":'',
            "seat_types":'',
            "train_date":''
        }

        pricesDic = {
            'A': '',
            'B': '',
            'C': '',
            'D': '',
            'E': '',
            'F': '',
            'G': '',
            'H': '',
            'I': '',
            'J': ''
        }

        item = items.split('|')

        price_data["train_no"] = item[2]
        price_data["from_station_no"] = item[16]
        price_data["to_station_no"] = item[17]
        price_data["seat_types"] = item[35]
        price_data["train_date"] = item[13][0:4]+'-'+item[13][4:6]+'-'+item[13][6:]
        url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={0}&from_station_no={1}&to_station_no={2}&seat_types={3}&train_date={4}".format(price_data["train_no"],price_data["from_station_no"],price_data["to_station_no"],price_data["seat_types"],price_data["train_date"])
        while 1:
            try:
                r_price = self.download.getData(url)
                if r_price.startswith(u'\ufeff'):
                    r_price = r_price.encode('utf8')[3:].decode('utf-8')
                    # print(r_price)
                r_price = json.loads(r_price)

                break
            except:
                continue
        price = r_price['data']
        price = dict(price)
        for i in range(0,1):
            A = ('A9' in price.keys())  # 商务座票价对应key是A9或者P
            if A == False:
                A = ('P' in price.keys())
                if A == False:
                    A = ''
                else:
                    A = price['P']
            else:
                A = price['A9']

            B = ('M' in price.keys())  # 一等座对应key为M
            if B == False:
                B = ''
            else:
                B = price['M']
            C = ('O' in price.keys())  # 二等座对应key为O
            if C == False:
                C = ''
            else:
                C = price['O']
            D = ('A6' in price.keys())
            if D == False:
                D = ''
            else:
                D = price['A6']
            E = ('A4' in price.keys())
            if E == False:
                E = ''
            else:
                E = price['A4']
            F = ('F' in price.keys())
            if F == False:
                F = ''
            else:
                F = price['F']
            G = ('A3' in price.keys())
            if G == False:
                G = ''
            else:
                G = price['A3']

            H = ('A2' in price.keys())
            if H == False:
                H = ''
            else:
                H = price['A2']
            I = ('A1' in price.keys())
            if I == False:
                I = ''
            else:
                I = price['A1']

            J = ('WZ' in price.keys())
            if J == False:
                J = ''
            else:
                J = price['WZ']
            pricesDic['A'] = A
            pricesDic['B'] = B
            pricesDic['C'] = C
            pricesDic['D'] = D
            pricesDic['E'] = E
            pricesDic['F'] = F
            pricesDic['G'] = G
            pricesDic['H'] = H
            pricesDic['I'] = I
            pricesDic['J'] = J
        return pricesDic




    def parser(self,lists):
        cont = []
        name = [
            "station_train_code",
            "from_station_name",
            'start_time',
            "lishi",
            "shangwu_num",
            "yideng_num",
            "erdeng_num",
            "superruanwo_num",
            "ruanwo_num",
            "dongwo_num",
            "yingwo_num",
            "ruanzuo_num",
            "yingzuo_num",
            "wuzuo_num",
            "qita_num",
            "beizhu_num"
        ]

        for items in lists:  # 遍历result的每一项
            # data字典用于存放每一车次的余票信息
            pricesDic = self.price_url(items)


            data = {
                "station_train_code": '',
                "from_station_name": '',
                "to_station_name": '',
                'start_time': '',
                'end_time': '',
                "lishi": '',
                "shangwu_num": '',
                "yideng_num": '',
                "erdeng_num": '',
                "superruanwo_num": '',
                "ruanwo_num": '',
                "dongwo_num": '',
                "yingwo_num": '',
                "ruanzuo_num": '',
                "yingzuo_num": '',
                "wuzuo_num": '',
                "qita_num": '',
                "beizhu_num": ''
            }
            item = items.split('|')  # 用"|"进行分割

            data['station_train_code'] = item[3]  # 车次在3号位置
            data['from_station_name'] = item[6]  # 始发站信息在6号位置
            data['to_station_name'] = item[7]  # 终点站信息在7号位置
            data['start_time'] = item[8]  # 出发时间信息在8号位置
            data['end_time'] = item[9] # 抵达时间在9号位置
            data['lishi'] = item[10]  # 经历时间在10号位置
            #data['shangwu_num'] = item[32] or item[25]+'\n'+pricesDic['A'] # 特别注意：商务座在32或25位置
            data['shangwu_num'] = (item[32] or item[25])+'\n'+color.blue(pricesDic['A']) # 特别注意：商务座在32或25位置
            data['yideng_num'] = item[31]+'\n'+color.blue(pricesDic['B'])  # 一等座信息在31号位置
            data['erdeng_num'] = item[30]+'\n'+color.blue(pricesDic['C'])  # 二等座信息在30号位置
            data['superruanwo_num'] = item[21]+'\n'+color.blue(pricesDic['D'])  # 高级软卧信息在31号位置
            data['ruanwo_num'] = item[23]+'\n'+color.blue(pricesDic['E'])  # 软卧信息在23号位置
            data['dongwo_num'] = item[27]+'\n'+color.blue(pricesDic['F'])  # 动卧信息在27号位置
            data['yingwo_num'] = item[28]+'\n'+color.blue(pricesDic['G'] ) # 硬卧信息在28号位置
            data['ruanzuo_num'] = item[24]+'\n'+color.blue(pricesDic['H'] ) # 软座信息在24号位置
            data['yingzuo_num'] = item[29]+'\n'+color.blue(pricesDic['I'] ) # 硬座信息在29号位置
            data['wuzuo_num'] = item[26]+'\n'+color.blue(pricesDic['G'])  # 无座信息在26号位置
            data['qita_num'] = item[22]  # 其他信息在22号位置
            data['beizhu_num'] = item[1]  # 备注在1号位置

            # 如果没有信息则用“-”代替
            for pos in name:
                if data[pos] == '':
                    data[pos] = '-'

            cont.append(data)
        tickets = []  # 存放所有车次的余票信息
        for x in cont:
            tmp = []
            try:
                for y in name:

                    if y == "from_station_name":

                        s = color.green(list(Stations().stations.keys())[list(Stations().stations.values()).index(x[y])]) + '\n' + \
                            color.red(list(Stations().stations.keys())[list(Stations().stations.values()).index(x['to_station_name'])])
                        tmp.append(s)
                    elif y == "start_time":
                        s = color.green(x[y]) + '\n' + color.red(x["end_time"])
                        tmp.append(s)
                    elif y == "station_train_code":
                        s = color.yellow(x[y])
                        tmp.append(s)
                    else:
                        tmp.append(x[y])
                tickets.append(tmp)
            except:
                continue
        self.display(tickets)  # 返回所有车次余票信息

    def display(self,tickets):
        ptable = PrettyTable('车次 出发/到达站 出发/到达时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他 备注'.split(' '))
        for ticket in tickets:
            ptable.add_row(ticket)
        print(ptable)