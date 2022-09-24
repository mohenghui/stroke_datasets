
from config import ProcessData
import platform

import re
import os

def svg2txt():
    txt_tail=".txt"
    svg_list=os.listdir(ProcessData.svg_path)
    makedirR(ProcessData.svg_path)
    makedirR(ProcessData.txt_path)
    for svg_file in svg_list:
        filename,tail=os.path.splitext(svg_file)
        svg_path=os.path.join(ProcessData.svg_path,svg_file)
        print(os.path.join(ProcessData.txt_path,filename+txt_tail))
        paths = open(os.path.join(ProcessData.txt_path,filename+txt_tail), "w+")
        
        file = open(svg_path)

        regex = re.compile(r'.*?\sd="(.*?)".*?') 

        while 1:
            line = file.readline()
            if not line:
                break
            res = regex.findall(line)    
            if(res != None):
                for g in res:
                    # print(g+"\n")
                    paths.write(g+"\n")

        file.close()
        paths.close()
def beint(tuple_list):
    return tuple([int(i) for i in tuple_list])

def makedirR(c_path, is_dir=True):
    if is_dir and not os.path.exists(c_path):
        os.mkdir(c_path)
    elif not is_dir and not os.path.exists(c_path):  # 文件新建上一级目录
        if platform.system().lower() == 'windows':
            tmp = '\\'.join(c_path.split('\\')[:-1])
        elif platform.system().lower() == 'linux':
            tmp = '/'.join(c_path.split('/')[:-1])
        if not os.path.exists(tmp):
            os.mkdir(tmp)

if __name__ == '__main__':
    svg2txt()