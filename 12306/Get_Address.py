"""Train tickets query via command-line.
Usage:
    tickets <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    from             出发车站
    to               终点站
    date             出发日期

Example:
    filename 南京 北京 2016-07-01
"""
from docopt import docopt
import datetime
from Station_Code import Stations
import re

class Get_Address(object):

    def get_address(self):
        info = {}
        #info['from_station'] = '重庆'
        #info['to_station'] = '成都'
        #info['from_date'] = '2018-11-20'
        from_stations = input('请输入始发站：\n')
        to_stations = input('请输入终点站：\n')
        from_date = self._get_train_date()
        return self.inputArgs(from_stations,to_stations,from_date)
        #arguments = docopt(__doc__)
        #return self.inputArgs(arguments['<from>'], arguments['<to>'], arguments['<date>'])
        #return info
    def _get_train_date(self):
        """
        获取出发时间，这个函数的作用是为了：时间可以输入两种格式：2016-10-05、20161005
        """
        train_date = input('请输入出发日期：\n')
        if len(train_date) == 8:
            return '{0}-{1}-{2}'.format(train_date[:4],train_date[4:6],train_date[6:])

        if '-' in train_date:
            return train_date
    def inputArgs(self,from_station, to_station, d):

        now_time = datetime.datetime.now()  # 当前日期
        # 校验
        flag1 = False
        flag2 = False
        flag3 = False

        while flag1 == False or flag2 == False or flag3 == False:
            from_index = list(Stations().stations).count(from_station)
            to_index = list(Stations().stations).count(to_station)
            # 始发站在车站列表中，并且始发站和终点站不同
            if from_index > 0 and to_station != from_station:
                flag1 = True
            # 终点站在车站列表中，并且始发站和终点站不同
            if to_index > 0 and to_station != from_station:
                flag2 = True
            rdate = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', d)
            if rdate:
                from_date = datetime.datetime.strptime(d, '%Y-%m-%d')
                sub_day = (from_date - now_time).days
                if 0 <= sub_day < 29:
                    flag3 = True
            if not flag1:
                print("始发站不合法！")
                from_station = input("请输入出发站：\n")
            if not flag2:
                print("终点站不合法！")
                to_station = input("请输入目的地:\n")
            if not flag3:
                print("出发日期不合法！")
                d = input("请输入出发日期(格式：年-月-日)：\n")
                from_date = datetime.datetime.strptime(d, '%Y-%m-%d')
                sub_day = (from_date - now_time).days
        info = {
            'from_station': '',
            'to_station': '',
            'from_date': ''
        }
        info['from_station'] = from_station
        info['to_station'] = to_station
        info['from_date'] = d
        return info

