#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "mn2pf9",
        "typeId": "Device",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data)
    m=cmd.data['command']
    print()
    if m == "lon":
        print("Motor is Switched ON")
    elif m == "loff":
        print("Motor is Switched OFF")
    print()    

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    gas = random.randint(0,100)
    myData={'temperature':temp, 'humidity':hum, 'gas' : gas}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
