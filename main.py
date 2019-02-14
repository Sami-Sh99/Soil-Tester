
#######################################
#Serial Communication with the arduino#
#######################################

import serial
import Twilio
import DatasetSort as pHmodel
import numpy as np
from time import sleep

# Your Account SID from twilio.com/console
account_sid=""
# Your Auth Token from twilio.com/console
auth_token=""

ard = serial.Serial('COM3',9600)#you might need to change the COM port according to your arduino
sleep(0.2)
def GetData():
	c='a'
	ard.flush()
	ard.write(c.encode('ascii'))
	read_serial=ard.readline()
	read_serial=read_serial.decode()
	read_serial=read_serial.split(" ")
	read_serial[-1]=read_serial[-1][0:-2]
	read_serial=[float(x) for x in read_serial]
	return(read_serial) #Returns a list  [Temp,Humidity,Moisture,LDR,IR,pH]

#Check the system by waiting for a signal from the arduino to finish the setup
print("Waiting for Arduino Setup")
while ard.in_waiting:
    pass
print("Rasbperry pi ready")
#In the main loop( a 400 iteration loop) measure data and store data,
data=[]
for i in range(400):
	Move(2000)
	data.append(GetData())

#analyze data
pH_data=[]
Moist_data=[]
for pH in data:
	pH_data.append(data[5])
for Moist in data:
	Moist_data.append(data[2])

np_pH=np.array(pH_data)
Avg_pH=np.mean(np_data)

np_Moist=np.array(Moist_data)
Avg_Moist=np.mean(np_data)

result=pHmodel.predict(Avg_pH,Avg_Moist)

text_msg="Your Soil is eligible to plant : {}".format(result)

send(text_msg,account_sid,auth_token)