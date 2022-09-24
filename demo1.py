# from wand.api import library
# import wand.color
# import wand.image
# #pip install Wand
# with wand.image.Image() as image:
#     with wand.color.Color('transparent') as background_color:
#         library.MagickSetBackgroundColor(image.wand, 
#                                          background_color.resource) 
#     svg_file = open(".\dataset\ch\color_svg\阿.svg","r")
#     image.read(blob=svg_file.read(), format="svg")
#     png_image = image.make_blob("png32")

# with open(".\dataset\ch\color_img\阿.png", "wb") as out:
#     out.write(png_image)