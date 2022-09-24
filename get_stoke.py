import os
import json
import natsort
from cairosvg import svg2png
import re
import random
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from config import ProcessData,StrokeColor
def get_json():
    # 数据路径
    path = "new_stoke.json"
    # 读取文件数据
    with open(path, "r") as f:
        row_data = json.load(f)
    print(len(row_data["⺊"].split(',')))
    # chinese=[]
    # stroke=[]
    # for i in row_data.keys():
    #     chinese.append(i.split(','))
    # print(chinese)
    # for i in row_data.values():
    #     stroke.append(i.split(','))
def get_txt():
    stroke={}

    for line in open("./stroke.txt", encoding='utf-8'):
        k,v=line.strip().split(':')
        # print(k,v)
        if k not in stroke:stroke[k]=v.split(',')
    # print(stroke["噥"])
def set_stroke():
    stroke={}
    for line in open("./stroke.txt", encoding='utf-8'):
        k,v=line.strip().split(':')
        # print(k,v)
        if k not in stroke:
            tmp_stroke=[]
            for i in v.split(','):
                if "/" in i:
                    tmp_stroke.append(i.split('/')[0])
                else:
                    tmp_stroke.append(i)
                stroke[k]=tmp_stroke
    # print(stroke["霭"])

    # print(stroke_all)
    # print(stroke)
    return stroke
def set_stroke_color():
    stroke={}
    stroke_color={}
    stroke_all=set()
    for line in open("./stroke.txt", encoding='utf-8'):
        k,v=line.strip().split(':')
        # print(k,v)
        if k not in stroke:
            tmp_stroke=[]
            for i in v.split(','):
                if "/" in i:
                    tmp_stroke.append(i.split('/')[0])
                    stroke_all.add(i.split('/')[0])
                else:
                    tmp_stroke.append(i)
                    stroke_all.add(i)
                stroke[k]=tmp_stroke
    # print(stroke["霭"])

    # print(stroke_all)
    for i in stroke_all:
        if i not in stroke_color:
            stroke_color[i]=random_color()
    print(len(stroke_color))
def rename_dir():
    svg_list=[]
    file_list=natsort.natsorted(os.listdir(ProcessData.save_svg_path))
    # print(file_list)
    for line in open("./graphics.txt", encoding='utf-8'):
        k=line.strip().split(":")[1].split(",")[0][1:-1]
        svg_list.append(k)
        # if k not in stroke:stroke[k]=v.split(',')
        # print(stroke["噥"])
    # print(svg_list)
    for idx,svg in enumerate(svg_list):
        old_name=os.path.join(ProcessData.save_svg_path,file_list[idx])
        new_name=os.path.join(ProcessData.save_svg_path,svg+".svg")
        os.rename(old_name,new_name)

    # print(len(svg_list),len(file_list))
def compare():
    lost_list=[]
    svg1=os.listdir("./dataset/ch/svg")
    svg2=os.listdir("./dataset/ch/svgs")
    for i in svg2:
        if i not in svg1:
            lost_list.append(i)
    print(lost_list)
def random_color():
    color_list=[]
    for _ in range(32):
        color_list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    # print(color_list)
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def get_color(label=True):
    tmp_svg=[]
    if not label:save_path=ProcessData.og_svg_path
    else:save_path=ProcessData.color_svg_path
    for line in open(ProcessData.tmp_txt, encoding="utf-8"):
        tmp_svg.append(line.strip())
    regex = re.compile(r'<path d=(.*?)></path>') 
    file_list=natsort.natsorted(os.listdir(ProcessData.save_svg_path))
    stroke_list=set_stroke()
    stroke_color=StrokeColor.stroke_color
    error_font=[]
    not_found=[]
    for file in file_list:
        file_name,tail=os.path.splitext(file)
        if file_name not in stroke_list:
            not_found.append(file_name)
            print(file_name+"：字没有找到")
            continue
        save_file_path=os.path.join(save_path,file)
        file_path=os.path.join(ProcessData.save_svg_path,file)
        file_controll = open(file_path)
        svg_txt=open(save_file_path,mode='w')
        result=[]
        index=0
        print(file)
        error_flag=False
        while 1:
            line = file_controll.readline()
            if not line:
                break
            res = regex.findall(line)   
            if(len(res) != 0):
                if index>=len(stroke_list[file_name]):
                    error_flag=True
                    break
                for i in res:
                    if not label:result.append('        <path d='+i+'></path>')
                    else:result.append('        <path d='+i+" fill='rgb"+str(stroke_color[stroke_list[file_name][index]])+"'></path>")
                    
                    index+=1
        if error_flag:
            print(file_name+"：字出错了")
            error_font.append(file_name)
            svg_txt.close()
            file_controll.close()
            os.remove(save_file_path)
            continue
        for i in range(3):
            if i==1 and not label:
                svg_txt.write('<rect width="100%" height="100%" fill="white" />'+"\n")
            else:
                svg_txt.write(tmp_svg[i]+"\n")
        for g in result:
            svg_txt.write(g+"\n")
        # for i in range(3,4):
        svg_txt.write(tmp_svg[3]+"\n")
        svg_txt.write(tmp_svg[4])
        svg_txt.close()
        file_controll.close()
    print(error_font)
    print(not_found)
def svg2img(label=False):
    if label:
        svg_path=ProcessData.color_svg_path
        save_img_path=ProcessData.color_img_path
    else:
        svg_path=ProcessData.og_svg_path
        save_img_path=ProcessData.og_img_path
    for file in os.listdir(svg_path):
        file_path=os.path.join(svg_path,file)
        file_name,tail=os.path.splitext(file)
        save_color_path=os.path.join(save_img_path,file_name+".png")
        pic = svg2rlg(file_path)
        print(file)
        renderPM.drawToFile(pic,save_color_path)
def svg2img2(label=True):
    if label:
        svg_path=ProcessData.color_svg_path
        save_img_path=ProcessData.color_img_path
    else:
        svg_path=ProcessData.og_svg_path
        save_img_path=ProcessData.og_img_path
    for file in os.listdir(svg_path):
        file_path=os.path.join(svg_path,file)
        file_name,tail=os.path.splitext(file)
        save_color_path=os.path.join(save_img_path,file_name+".png")
        # pic = svg2rlg(file_path)
        print(file)
        # renderPM.drawToFile(pic,save_color_path)
        svg2png(url=file_path, write_to=save_color_path)
if __name__=="__main__":
    # get_txt()
    # rename_dir()
    # rename_dir()
    # random_color()
    # fill="rgb(91,158,86)"
    # get_color()
    # svg2img()
    svg2img2()