import os
from PIL import Image


def main():
    # This program copies images from Windows Spotlight folder and adds .jpg
    # to them.
    impath = "C:\\Users\\Jan\\AppData\\Local\\Packages\\Microsoft.Windows."+\
             "ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
    folder = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\nove\\"
    rootf = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\"
    rootfl = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\landscape\\"  # landscape
    rootfp = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\portrait\\"  # portrait
    szthshld = 200e3  # [Bytes] SiZe THreSHoLD
    ims = os.listdir(impath)
    imsr, imsl, imsp = os.listdir(rootf), os.listdir(rootfl), os.listdir(rootfp)
    for i in ims:
        if os.path.getsize(impath+i) >= szthshld:
            with Image.open(impath+i) as img:
                w, h = img.size
            if (w>=h) and ((i+".jpg" not in imsr) and (i+".jpg" not in imsl)):
                os.system("copy "+impath+i+" "+folder+i+".jpg")
            elif (w<h) and ((i+".jpg" not in imsr) and (i+".jpg" not in imsp)):
                os.system("copy "+impath+i+" "+folder+i+".jpg")


if __name__ == "__main__":
    main()
