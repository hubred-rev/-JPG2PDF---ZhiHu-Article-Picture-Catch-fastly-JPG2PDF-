import os,sys
from PIL import Image
imgs=[]
for a in os.walk(sys.path[0]):
    a[2].sort()
    for b in a[2]:
        if b[-3:]=='jpg':
            imgs.append(Image.open(b))
            imgs[len(imgs)-1].convert('RGB')
img=imgs[0]
imgs=imgs[1:]
img.save(r'document.pdf',save_all=True,append_images=imgs)
