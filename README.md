# PiRemoteRecorder
Simple code to be loaded on all Rasperry Pis to easily record video from remote access (ssh)

## Prepare devices
- Install respberry pi OS (with or without desktop)
- activate ssh on the device
- connect it to the same network of your computer
- install prerequisites
```
sudo apt update
sudo apt upgrade
sudo apt install screen
sudo apt install git

git clone https://github.com/massimodeagro/PiRemoteRecorder.git
```

## Run
- activate network
- turn on raspberry
- connect pc to network
- open powershell as admin. Run
```
arp -a
```

this will check for devices connected to network

find ip for the corresponding MAC address (check phone connected devices for pi hostname/mac correspondance)

- now open WSL terminal
- connect to device
```
ssh -Y username@ip.found.in.arp
```
- insert password
- now you are inside the raspi terminal. The user@hostname should be green
- move to the software folder
```
cd PiRemoteRecorder
```

- run camera check
```
python preview.py
```

- if everything is ok, you can now proceed with recording
  
```
screen -S nameOfHangedTerminal
python record.py
```

- you can close the terminal now. Next time you can
```
screen -r
```

then

```
exit
```

- if you want to move a video from the raspberry to the main computer without extracting the sd card, you can do so using ssh copy.
- From the local WSL terminal, type

```
scp username@ip.found.in.arp:/path/to/video/videoname.format /path/to/local/videoname.format
```


