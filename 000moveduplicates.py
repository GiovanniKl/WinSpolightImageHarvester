import os
import numpy as np
from PIL import Image

SIZE = 128, 128


def main():
    """
    This program reads images in given folders (landscape and/or
    portrait) and checks for possible duplicates.

    Although only images with unique names are present, there are still
    some duplicates.  Since Microsoft updates the image names from
    time to time, they have a time tag.
    Oldest images are kept, newer moved to duplicates.
    """
    # root folders
    rootfl = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\landscape\\"  # landscape
    rootfp = "C:\\Users\\Jan\\Pictures\\WinSpotlight\\portrait\\"  # portrait
    # duplicates folder in each root
    dupf = "duplicates\\"

    for i in [rootfl, rootfp]:
        find_move_dups(i, dupf)


def find_move_dups(rootf, dupf):
    """Finds and moves (newer) duplicates to dupf folder."""
    ndups = 0  # number of found duplicates
    dups = []  # names of duplicates
    tested = []  # list of already tested images
    ims = os.listdir(rootf)
    while set(tested) != set(ims):
        for i in ims:  # cycle until unchecked image found
            if i in tested:
                continue
            if os.path.splitext(i)[1] != ".jpg":
                tested.append(i)  # just a precaution
                continue
            break
        dups.append(i)
        img0 = Image.open(rootf+i)
        img0.thumbnail(SIZE)
        img0ar = np.asarray(img0)
        for j in ims:  # cycle thru all (not like the i cycle)
            if j in tested or j == i:
                continue
            if os.path.splitext(j)[1] != ".jpg":
                continue
            with Image.open(rootf+j) as img1:
                img1.thumbnail(SIZE)
                if np.all(np.isclose(img0ar, np.asarray(img1), 0.2, 15)):
                    dups.append(j)
        keep, move = eval_mtime(rootf, dups)
        ndups += len(move)
        print(len(move), end=" ")
        # move the dups
        for j in move:
            os.system('move "'+rootf+j+'" "'+rootf+dupf+'"')
        # reset the search
        tested.append(keep)
        ims = os.listdir(rootf)
        dups = []
    print(f"\nAll duplicates moved. {ndups} duplicate images found.")


def eval_mtime(rootf, dups):
    """Evaluates the modification time of the images.
    File with smallest time is to kept, rest is to be moved.
    """
    times = []
    for i in dups:
        times.append(os.path.getmtime(rootf+i))
    imin = np.argmin(times)
    return dups[imin], dups[:imin]+dups[imin+1:]


if __name__ == "__main__":
    main()
