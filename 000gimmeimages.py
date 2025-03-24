import os
from PIL import Image


def main():
    """Copies images from Windows Spotlight folder and adds .jpg to them.
    """
    impath = "C:\\Users\\Jan\\AppData\\Local\\Packages\\Microsoft.Windows."+\
             "ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
    folder = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\new\\"
    rootf = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\"
    rootfl = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\landscape\\"  # landscape
    rootfp = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\portrait\\"  # portrait
    dupf = "duplicates\\"  # duplicates
    szthshld = 200e3  # [Bytes] SiZe THreSHoLD
    ims = os.listdir(impath)
    imsr = os.listdir(rootf)
    imsl = os.listdir(rootfl) + os.listdir(rootfl+dupf)
    imsp = os.listdir(rootfp) + os.listdir(rootfp+dupf)
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
