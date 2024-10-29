# This is a sample Python script, main文件.

import os
import sys

from service.draw import Draw
from util.config_reader import ConfigReader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 统一执行路径
    project_root = os.path.dirname(os.path.abspath(__file__))

    # 添加项目路径到 sys.path
    sys.path.append(project_root)
    print('project_root = ', project_root)

    # 获取名字列表
    config_reader = ConfigReader(project_root + '/conf/config.ini')
    name_list = config_reader.get_name_list()
    print('name list length = ', len(name_list))

    # 获取字库位置
    ttc = config_reader.get_ttf()
    print('ttc = ', ttc)

    # 原始图片
    master_pic = project_root + "/assets/air.jpg"

    # 往图片上加入名字，并保存
    draw = Draw()
    for name in name_list:
        print("name = ", name)
        draw.draw_str(project_root, master_pic, ttc, name)
