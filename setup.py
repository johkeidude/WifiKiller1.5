import os
import time
print("Downloading mdk3")
time.sleep(1)
os.system("wget http://de.archive.ubuntu.com/ubuntu/pool/universe/m/mdk3/mdk3_6.0-4_amd64.deb")
os.system("sudo dpkg -i mdk3_6.0-4_amd64.deb")
print("Downloading wash")
time.sleep(1)
os.system("sudo apt-get install aircrack-ng reaver")
print("DONE!")
