"""
Nama Tools: ANTI BAN ON OFF Data OTOMATIS
By: ./CHAOSUE4
Group: @UE4Esports
"""
import os, time, sys
print "Nama Tools: ANTI BAN ON OFF Data OTOMATIS"
print "@UE4Esports\n"
def offon():
    os.system('su -c "svc wifi enable"')
    time.sleep(1)
    print("Wifi On")
    time.sleep(240)
    os.system('su -c "svc wifi disable"')
    print("Wifi Off")
    return offon()

if __name__ == '__main__':
    offon()
     
