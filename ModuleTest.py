import Twilio
import GeoLocation
import DatasetSort as pHmodel

Global_Positon=GeoLocation.getLocation()
plant=pHmodel.predict(6.3)
Twilio.send("Let's start working!! I am now at :{} and going to plant : {}".format(Global_Positon,plant))
