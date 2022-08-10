# WinSpolightImageHarvester
Set of scripts for acquiring images from Windows Spotlight lockscreen backgrounds (Win 10/11).

## Prerequisites
- Operating system Windows 10 or 11 (I did not check for compatibility with other systems).
- Installed Python 3 (scrips were written in Python 3.7).
- installed python packages `os` and `Pillow`.

## How to begin
To start, download all repository files and put them in a desired folder in your PC where all WindowsSpotlight images will be stored. 

After this, you need to update paths in the `000gimmeimages.py` and `000sortimages.py` python scripts (written in Python 3.7):
- `impath` - Path to the Windows Spotlight folder, usual structure is `C:\Users\<username>\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_<some characters>\LocalState\Assets\` (not present in `000sortimages.py`).
- `folder` - Folder where to download new images, usual structure is `<path to the base folder of this project>\new\`.
- `rootf` - Base folder of this project, usual structure is `<path to the base folder of this project>\`.
- 'rootfl' - Folder for landscape-oriented images, usual structure is `<path to the base folder of this project>\landscape\`.
- 'rootfp' - Folder for portrait-oriented images, usual structure is `<path to the base folder of this project>\portrait\`.
Due to python string handling, use `\\` instead of `\` in the script (applies to all python scripts in this project). All paths must end with a `\`, resp. `\\`.

Then create folders for landscape and portrait images - names must correspond to the ones mentioned in the python scripts.

Program `del_all_images_here.bat` should be located in `folder` path. *Note: your antivirus may ask you whether to trust this program, allow it to function properly. Please note that this program is voluntary.*

It is convenient to add a shortcut of your base folder in the `folder`.

## How to use

Whenever you see a nice picture on your lockscreen, run `000gimmeimages.py`. Then look in the `folder` and move images you want to save in the shortcut of your base folder (or move them in the parent folder by hand). If there are some images you don't want to save, delete them or use the `del_all_images_here.bat` program (do so after you move all nice images to parent folder, this program deletes all .jpg files in the `folder`).

When you feel like miximg up portrait and landscape images is not to your liking, run the `000sortimages.py` script.

**Enjoy!**