import time
from pymycobot import MyCobot280
mc = MyCobot280("/dev/ttyAMA0",1000000)
mc.sync_send_angles([-90,2,0,2,2,-45],50)
mc.set_gripper_state(0,10)
time.sleep(0.1)
mc.sync_send_angles([-90,-50,-30,20,2,-45],70)
mc.sync_send_angles([-90,-90,100,-20,2,-45],70)
mc.sync_send_angles([-90,-130,12,115,2,-45],70)
time.sleep(0.1)
mc.set_gripper_state(1,10)
time.sleep(1)

mc.sync_send_angles([-90,2,0,2,2,-45],50)
mc.sync_send_angles([-90,-90,100,-20,2,-45],70)
mc.set_gripper_state(0,10)
mc.sync_send_angles([-90,2,0,2,2,-45],50)