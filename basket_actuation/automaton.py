#remember to configure and enable I2C in sudo raspi-config.

from mpu6050 import mpu6050 as IMU #install mpu6050-raspberrypi
from time import sleep as wait
import threading as thr

#// ============ AUTO VARS ============ //#
#// do not touch these pls, 
# or you'll ruin the program
IMUdata={} #/ Data Dictionary

def IMUdata_module():
    global IMUdata
    IMU_1=IMU(0x68)
    while True:
        IMUdata["Acceleration"]=IMU_1.get_accel_data()
        IMUdata["Gyro"]=IMU_1.get_gyro_data()
        wait(seconds=1)

IMUt=thr.Thread(target=IMUdata_module)
IMUt.start()
IMUt.join()

    