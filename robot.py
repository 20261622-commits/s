import time
from pymycobot import MyCobot280
mc = MyCobot280("/dev/ttyAMA0",1000000)
mc.sync_send_angles([-90,2,0,2,2,-45],50)

for _ in range(3):
    mc.sync_send_angles([-90,30,-20,20,90,-45],60,timeout=2)

    #left
    mc.sync_send_angles([-90,-40,20,-20,90,-45],60,timeout=2)

for _ in range(1):
    mc.sync_send_angles([2,50,-60,2,2,-45],60,timeout=1)

    #left
    mc.sync_send_angles([2,20,-85,-20,2,-45],60,timeout=1)
    mc.sync_send_angles([50,50,-60,2,2,-45],60,timeout=0)
    mc.sync_send_angles([30,20,-85,-20,2,-45],60,timeout=0)
    mc.sync_send_angles([-30,50,-60,2,2,-45],60,timeout=0)
    mc.sync_send_angles([-50,20,-85,-20,2,-45],60,timeout=0)
    mc.sync_send_angles([-90,50,-85,2,2,-45],60,timeout=1)
    mc.sync_send_angles([-120,20,-85,-20,2,-45],60,timeout=1)

mc.sync_send_angles([-90,2,0,2,2,-45],50)
time.sleep(2)
