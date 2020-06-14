

# Detailed description

![logo](/assets/logo.png)

## Introduction

Using mobile devices GPS and IBM Watson’s Image Recognition AI, Waterfall aims to be a quicker response system that can optimise the transfer of crucial information of emergency situations from first responders to SCDF emergency operators. Through the use of geolocational web APIs and open source datasets of accidents and fires, Waterfall is able to accurately provide information to SCDF personnel in a timely manner and minimise emergency response time.

Being at the scene of an incident may be terrifying and stressful, which is why Waterfall can create a seamless process for first responders to report emergency situations that can not only save time but also be more accurate.

## Features

When the responder opts to message 995, or if SCDF hotline is overcrowded, they will receive an SMS link to our Website, Waterfall. There they will report the incident they have witnessed by uploading a photo of the incident. 

Utilising a photos option instead of text or criteria selection, we minimise the time taken for the user to provide vital information. The photo then can be analysed by our Image Recognition AI

## Image Recognition

The image is then sent to the IBM Cloudant database, where image recognition API will be used to identify and classify the emergency situation (e.g. Fire or/and Traffic Accident) and their severity. This can allow emergency operators to appropriately dispatch personnel to counter the situation.

This approach will also be more efficient and quicker compared to simply relying on auditory accounts from the first responders, who may not have appropriate knowledge to accurately assess the severity of the situation.

## Use of Geolocational API

Emergency operators can also obtain the accurate location of the incident through the photo’s and device’s geolocational tag. This can be especially useful when the responder does not have information on where exactly the incident is, or when the incident has occurred in more locations that do not have an exact address.

Furthermore, the use of these tags will make accessing the location faster, as emergency operators will immediately obtain the location, rather than have to find it after the responders have told them where it is. This is especially useful when the location does not have a distinct feature, e.g. middle of PIE, how far into the middle? Which lane?. A GPS location would be extremely useful in determining the exact location, especially with the high accuracy of GPS locations in latest mobile devices.

## Natural Language Processing (NLP) Translation

Emergency operators are able to use the NLP translator when the responder that calls in is unable to speak English. This is especially useful since a big portion of the aging and vulnerable population is unable to speak in English. With the NLP translation, there will be minimal delay in the communication between the emergency operators and the responder. This minimises emergency response time to provide timely treatment.

## Text to Speech
To provide responders with assistance and reassurance, helpful guides on what to do while waiting for help will be provided in the form of both text and audio. By clicking on the audio button on the responder website, the text will be read aloud to responders. This will be extremely useful to the vulnerable populations that may have difficulty with reading the text guides.


## Conclusion

Waterfall is the solution that minimises emergency response time by using technology and data analytics to provide quicker and better aid as well as potentially save more lives in emergency situations.

