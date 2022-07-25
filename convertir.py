from PIL import Image

im = Image.open("itemshop.png")
rgb_im = im.convert('RGB')
rgb_im.save('itemshop.jpg')