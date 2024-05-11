import os
import shutil

# source = r"/Users/prakashpali/Google Drive/My Drive/07_Photos/00_Shadi_ki_tasveerein/Day02/Beach Side"
source = r"/Users/prakashpali/Library/CloudStorage/GoogleDrive-pali.14192@gmail.com/My Drive/07_Photos/00_Shadi_ki_tasveerein/Day02/Beach Side/CAM -02"
destination = r"/Users/prakashpali/Library/Mobile Documents/com~apple~CloudDocs/google_drive/My Drive/07_Photos/00_Shadi_ki_tasveerein/Day02/Beach Side/CAM -02"

# gather all files
allfiles = os.listdir(source)

# iterate on all files to move them to destination folder
for f in allfiles:
    src_path = os.path.join(source, f)
    dst_path = os.path.join(destination, f)
    shutil.move(src_path, dst_path)