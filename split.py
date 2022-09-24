import os
from config import ProcessData
from utils import makedirR
if __name__ == '__main__':
    tp_files = os.listdir(ProcessData.root_path)
    img_tail = ['.txt']
    annotation_tail = ['.svg']
    makedirR(ProcessData.svg_path)
    makedirR(ProcessData.txt_path)
    for file in tp_files:
        file_path = os.path.join(ProcessData.root_path, file)
        if os.path.isdir(file_path):
            continue
        file_tail = os.path.splitext(file)[1].lower()
        if file_tail in img_tail:
            new_path = os.path.join(ProcessData.svg_path, file)
            os.rename(file_path, new_path)
        elif file_tail in annotation_tail:
            new_path = os.path.join(ProcessData.txt_path, file)
            os.rename(file_path, new_path)
