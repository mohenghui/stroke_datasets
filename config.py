class ProcessData():
    svg_path="./dataset/ch/svg"
    img_path="./dataset/ch/jpg"
    txt_path="./dataset/ch/txt"
    root_path="./dataset/ch/svg"
    dict_txt="./dataset/ch/graphics.txt"
    save_svg_path="./dataset/ch/save_svg"
    color_svg_path="./dataset/ch/color_svg"
    tmp_txt="tmp_svg.txt"
    color_img_path="./dataset/ch/color_img"
    og_svg_path="./dataset/ch/og_svg"
    og_img_path="./dataset/ch/og_img"
# class SplitData():
#     annotation_path="./svg"
#     img_path="./txt"
class StrokeColor():
    # stroke_color={"横":(184, 50, 182),"竖":(51, 230, 181),"点":(52, 102, 53),
    # "撇":(22, 204, 160),"横折":(23, 0, 16),"横折折折钩":(8, 214, 39),
    # "竖钩":(224, 127, 188),"竖提":(235, 212, 28),"竖弯钩":(181, 115, 157),
    # "捺":(114, 47, 192),"横撇":(48, 210, 244),"竖折":(105, 17, 37),
    # "横折钩":(120, 62, 101),"":()}
    # stroke_color={'竖钩': (80, 168, 82), '竖折撇': (121, 5, 233), '横折弯钩': (45, 110, 95),
    # '弯钩': (79, 182, 181), '横折折折钩': (91, 99, 36), '横折提': (210, 55, 84), 
    # '横折': (0, 237, 38), '横折钩': (17, 221, 32), '撇折': (204, 233, 81), 
    # '横折折撇': (104, 234, 152), '竖弯钩': (127, 219, 202), '撇': (191, 51, 105), 
    # '捺': (139, 112, 6), '点': (52, 101, 178), '竖提': (172, 91, 99), 
    # '竖': (121, 177, 26), '竖折折钩': (235, 142, 246), '横折折': (187, 174, 203),
    # '斜钩': (242, 187, 87), '横折折折': (188, 101, 185), '横': (104, 96, 167), 
    # '撇点': (31, 224, 112), '竖折': (29, 201, 247), '提': (94, 207, 156), '横撇': (58, 214, 206)}
    stroke_color={'竖钩': (1,1 , 1), '竖折撇': (2, 2, 2), '横折弯钩': (3, 3, 3),
    '弯钩': (4, 4, 4), '横折折折钩': (5, 5, 5), '横折提': (6, 6, 6), 
    '横折': (7, 7, 7), '横折钩': (8, 8, 8), '撇折': (9, 9, 9), 
    '横折折撇': (10, 10, 10), '竖弯钩': (11, 11, 11), '撇': (12, 12, 12), 
    '捺': (13, 13, 13), '点': (14, 14, 14), '竖提': (15, 15, 15), 
    '竖': (16, 16, 16), '竖折折钩': (17, 17, 17), '横折折': (18, 18, 18),
    '斜钩': (19, 19, 19), '横折折折': (20, 20, 20), '横': (21, 21, 21), 
    '撇点': (22, 22,22 ), '竖折': (23, 23, 23), '提': (24, 24, 24), '横撇': (25, 25, 25)}

class ErrorFont():
    pass
#     '剮.svg', '剳.svg', '務.svg', '勵.svg', '勸.svg', '厲.svg', '咼.svg', '嘩.svg', '嚄.svg', '嚴.svg', '囈.svg', '囌.svg', '塊.svg', '夢.svg', '媧.svg', '寬.svg', '巖.svg', '廣.svg', '彟.svg', '懞.svg', '戠.svg', '拋.svg', '撾.svg', '擴.svg', '敻.svg', '暱.svg', '曄.svg', '曚.svg', '條.svg', '棻.svg', '楛.svg', '樺.svg', '櫆.svg', '權.svg', '歔.svg', '歡.svg', '渦.svg', '滌.svg', '澠.svg', '濛.svg', '瀟.svg', '為.svg', '爇.svg', '爌.svg', '犂.svg', '獲.svg', '獷.svg', '瓊.svg', '癘.svg', '癢.svg', '皙.svg', '矇.svg', '礦.svg', '禍.svg', '禸.svg', '穫.svg', '窩.svg', '竈.svg', '糢.svg', '糲.svg', '絛.svg', '縧.svg', '繩
# .svg', '繭.svg', '脩.svg', '臟.svg', '舊.svg', '艻.svg', '苧.svg', '苲.svg', '茀.svg', '茲.svg', '荊.svg', '莊.svg', '莖.svg', '莢.svg', '莧.svg', '莿.svg', '華.svg', '萊.svg', '萠.svg', '萬.svg', '葄.svg', '葉.svg', '葦.svg', '葷.svg', '蒐.svg', '蒓.svg', '蒔.svg', '蒞.svg', '蒟.svg', '蒭.svg', '蒻.svg', '蒼.svg', '蓂.svg', '蓋.svg', '蓔.svg', '蓮.svg', '蓴.svg', '蓽.svg', '蔔.svg', '蔣.svg', '蔥.svg', '蔭.svg', '蕎.svg', '蕑.svg', '蕓.svg', '蕕.svg', '蕘.svg', '蕠.svg', '蕢.svg', '蕩.svg', '蕪.svg', '蕭.svg', '蕷.svg', '薈.svg', '薊.svg', '薌.svg', '薑.svg', '薔.svg', '薦.svg', '薩.svg', '薳.svg', '薶.svg', '薺.svg', '藇.svg', '藍.svg', '藒.svg', '藘.svg', '藝.svg', '藥.svg', '藨.svg', '藪.svg', '藭.svg', '藹.svg', '藺.svg', '蘄.svg', '蘆.svg', '蘇.svg', '蘊.svg', '蘋.svg', '蘘.svg', '蘚.svg', '蘞.svg', '蘢.svg', '蘭.svg', '蘵.svg', '蘺.svg', '蘿.svg', '蝸.svg', '蠅.svg', '蠣.svg', '蠨.svg', '衊.svg', '襖.svg', '襪.svg', '襯.svg', '觀.svg', '諾.svg', '謊.svg', '謨.svg', '護.svg', '豱.svg', '貓.svg', '贅.svg', '躉.svg', '躪
# .svg', '過.svg', '邁.svg', '醜.svg', '鋩.svg', '錚.svg', '錨.svg', '鍋.svg', '鑊.svg', '铓.svg', '闞.svg', '霧.svg', '顴.svg', '養.svg', '饃.svg', '饈.svg', '驀.svg', '驊.svg', '驚.svg', '骯.svg', '髒.svg', '體.svg', '髕.svg', '髖.svg', '鬮.svg', '魆.svg', '魎.svg', '魖.svg', '魘.svg', '鯗.svg', '鰲.svg', '鶓.svg', '鶻.svg', '黽.svg', '黿.svg', '鼂.svg', '鼉.svg', '龜.svg'