import re
import os
from unittest import result
tmp_txt="tmp_svg.txt"
svg_dir="./dataset/ch/svgs"
save_dir="./dataset/ch/save_svg"
tmp_svg=[]
for line in open(tmp_txt, encoding="utf-8"):
  tmp_svg.append(line.strip())
# paths = open("paths.txt", "w+")

# tmp_svg="<svg version="1.1" width="64" height="64" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">"
regex = re.compile(r'<path d=(.*?) fill="lightgray"></path>') 
file_dir=os.listdir(svg_dir)

for file in file_dir:
  file_path=os.path.join(svg_dir,file)
  save_file_path=os.path.join(save_dir,file)
  file = open(file_path)
  svg_txt=open(save_file_path,mode='w')
  result=[]
  while 1:
    line = file.readline()
    # print(line)
    if not line:
      
      break
    res = regex.findall(line)   
    # print(res)
    # res=str(res)
    # print(res)
    if(len(res) != 0):
      for i in res:
        result.append('        <path d='+i+'></path>')

  for i in range(2):
    svg_txt.write(tmp_svg[i]+"\n")
  for g in result:
    svg_txt.write(g+"\n")
  for i in range(2,4):
    svg_txt.write(tmp_svg[i]+"\n")
  svg_txt.close()
  file.close()