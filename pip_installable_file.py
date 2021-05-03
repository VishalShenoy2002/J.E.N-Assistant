import os
import sys

python_path=sys.path[6]
packages=["pyttsx3","datetime","wikipedia","random","opencv-python","phonenumbers","pillow","tqdm"]

os.system("cd {}".format(python_path))
for package in packages:
    os.system("pip install {}".format(package))
    print('Installed {} Successfully'.format(package))