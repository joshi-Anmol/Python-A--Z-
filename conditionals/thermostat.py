device_status= "active"
temprature = 28 

if device_status == "active":
    if temprature>35 :
        print("Alert! The temprature is too hot")
    else :
        print("Temprature is normal ")    
else :
    print("Device is offline")        
     