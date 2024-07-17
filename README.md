# PiRemoteRecorder
Simple code to be loaded on all Rasperry Pis to easily record video from remote access (ssh)

1 - activate hotspot
2 - turn on raspberry
3 - connect pc to network

4 - open powershell as admin. Run
arp -a

find ip for the corresponding MAC address (check phone connected devices for pi hostname/mac correspondance)

5 - now open WLS terminal

6 - connect to device
ssh -Y livia@ip.found.in.arp

7 - insert password

8 - now you are inside the raspi terminal. The user@hostname should be green

9 - run camera check
python preview.py

10 - if everything is ok, you can now proceed with recording!!!!!!
screen -S nameOfHangedTerminal
python record.py

11 - you can close the terminal now. Next time you can
screen -r

then

exit
