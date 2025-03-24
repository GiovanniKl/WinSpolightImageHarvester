import os
from PIL import Image


def main():
    """This program sorts images in its folder to landscape and
    portrait folders based on the dimesions (w>=h or w<h).
    """
    rootf = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\"
    rootfl = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\landscape\\"  # landscape
    rootfp = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\portrait\\"  # portrait
    ims = os.listdir(rootf)
    for i in ims:
        if os.path.splitext(i)[1] != ".jpg":
            continue
        with Image.open(rootf+i) as img:
            w, h = img.size
        if w >= h:
            os.system("move "+rootf+i+" "+rootfl)
        else:
            os.system("move "+rootf+i+" "+rootfp)


if __name__ == "__main__":
    main()
