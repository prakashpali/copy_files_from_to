# Python program to demonstrate
# shutil.copytree()


# importing modules
import shutil


# Source path
# src = r"/Users/prakashpali/Google Drive/My Drive/06_Insta_Youtube/Ladakh Sept 2021/Day3_Leh_to_Khardungla_Diskit_Hunder"
src = r"/Users/prakashpali/Library/CloudStorage/GoogleDrive-pali.14192@gmail.com/Other computers/Thinkpad/00_KaamKiChiz/05_Photos/GoPro-Exports/2nd Oct"

# Destination path
# dest = r"/Users/prakashpali/Library/Mobile Documents/com~apple~CloudDocs/google_drive/My Drive/06_Insta_Youtube/Ladakh Sept 2021/Day3_Leh_to_Khardungla_Diskit_Hunder"
dest = r"/Users/prakashpali/Library/Mobile Documents/com~apple~CloudDocs/google_drive/Other computers/Thinkpad/00_KaamKiChiz/05_Photos/GoPro-Exports/2nd Oct"

# Copying the contents from Source
# to Destination without some
# specified files or directories
# shutil.copytree(src, dest, ignore = shutil.ignore_patterns('*.txt', 'a'))
shutil.copytree(src, dest)