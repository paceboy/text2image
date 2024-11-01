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

    op_name_list = config_reader.get_op_name_list()
    print('op name list length = ', len(op_name_list))

    # 获取字库位置
    ttc = config_reader.get_ttf()
    print('ttc = ', ttc)

    # 运营者的结业证书图片
    op_pic = project_root + "/assets/op_certificate.jpg"

    # 共读者的结业证书图片
    read_pic = project_root + "/assets/read_certificate.jpg"

    # 往图片上加入名字，并保存
    draw = Draw()
    for name in op_name_list:
        print("name = ", name)
        draw.draw_str(project_root, op_pic, ttc, name)

    for name in name_list:
        print("name = ", name)
        draw.draw_str(project_root, read_pic, ttc, name)
