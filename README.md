
# What’s the problem?

During traditional emergency voice calls, people may panic and it would take time to convey important information for SCDF Operators to dispatch. However, time is key in such emergencies and every second could make the difference between life and death.

# How can technology help?

Web technology, analytics and machine learning can be used for increased effectiveness in communication of detailed and reliable information for such emergency situations, which can help to minimise emergency response time.

# The idea

![slogan](/assets/slogan.png)

Waterfall is a web platform which utilises IBM cloud’s machine learning and AI for effective relaying of information between responders and SCDF personnel to provide even faster emergency response time.

It consists of a responder mobile website and a SCDF personnel administrative website. In the case of an emergency, First Responders can opt to message 995, to receive a SMS link to our website, Waterfall.

Using Waterfall, instead of the traditional voice-call to relay information slowly, responders can upload photographs of the situation and provide geo-location tags from the mobile phone’s in-built GPS. By leveraging IBM cloud’s image recognition, images uploaded will be used to assess and immediately classify the emergency situation accurately in real-time.

These essential information will be clearly displayed as a dashboard on Waterfall for SCDF personnel. Waterfall will also give helpful guides to responders and these guides are translated to multiple languages using the IBM Watson Translator.

# The architecture of your proposed solution
![architecture](/assets/architecture.png)

# Detailed description

![logo](/assets/logo.png)

## Introduction

Using mobile devices GPS and IBM Watson’s Image Recognition AI, Waterfall aims to be a quicker response system that can optimise the transfer of crucial information of emergency situations from first responders to SCDF emergency operators. Through the use of geolocational web APIs and open source datasets of accidents and fires, Waterfall is able to accurately provide information to SCDF personnel in a timely manner and minimise emergency response time.

Being at the scene of an incident may be terrifying and stressful, which is why Waterfall can create a seamless process for first responders to report emergency situations that can not only save time but also be more accurate.

## Features

When the responder opts to message 995, or if SCDF hotline is overcrowded, they will receive an SMS link to our Website, Waterfall. There they will report the incident they have witnessed by uploading a photo of the incident. 

Utilising a photo option instead of text or criteria selection, we minimise the time taken for the user to provide vital information. The photo then can be analysed by our Image Recognition AI

## Image Recognition

The image is then sent to the IBM Cloudant database, where image recognition API will be used to identify and classify the emergency situation (e.g. Fire or/and Traffic Accident) and their severity. This can allow emergency operators to appropriately dispatch personnel to counter the situation.

This approach will also be more efficient and quicker compared to simply relying on auditory accounts from the first responders, who may not have appropriate knowledge to accurately assess the severity of the situation.

## Use of Geolocational API

Emergency operators can also obtain the accurate location of the incident through the photo’s and device’s geolocational tag. This can be especially useful when the responder does not have information on where exactly the incident is, or when the incident has occurred in more locations that do not have an exact address.

Furthermore, the use of these tags will make accessing the location faster, as emergency operators will immediately obtain the location, rather than have to find it after the responders have told them where it is. This is especially useful when the location does not have a distinct feature, e.g. middle of PIE, how far into the middle? Which lane?. A GPS location would be extremely useful in determining the exact location, especially with the high accuracy of GPS locations in latest mobile devices.

## Natural Language Processing (NLP) Translation

Emergency operators are able to use the NLP translator when the responder that calls in is unable to speak English. This is especially useful since a big portion of the aging and vulnerable population is unable to speak in English. With the NLP translation, there will be minimal delay in the communication between the emergency operators and the responder. This minimises emergency response time to provide timely treatment.

## Conclusion

Waterfall is the solution that minimises emergency response time by using technology and data analytics to provide quicker and better aid as well as potentially save more lives in emergency situations.

# Project Roadmap / Proposed timeline

![roadmap](/assets/roadmap.png)

Our group has developed a working prototype at the link given (Please contact us if the website is not up, as IBM Cloud Foundry Free Tier will stop running after a few days of inactivity. Some of the AI have API limits as well, do let us know if there are any issues with the features mentioned). 

However, we faced several limitations due to the free tiers of the cloud technologies.

- IBM Watson - Free Tier Visual Recognition

The free tier only allowed for 1,000 images to be classified/trained, which gives us a very hard limit, as we are only able to train 500 images and leave the 500 for demo and prototyping purposes. With funding, we will be able to train the model on our entire dataset, which will further increase the accuracy of the image recognition system.

- Twilio SMS - Free Tier not inclusive of Singaporean numbers

The free tier does not allow SMS to numbers, and thus not available for development or prototyping. To purchase a Singaporean number for SMS purposes, they require $75/mth. In the future, we plan to make the website easily accessible via a SMS url link, therefore this will be in our projected roadmap.

- Google Maps - Free Tier Google Cloud Platform

We cannot access Google Maps API without adding billing. In the future, we plan to have a real-time updated map on the dashboard which will show the exact location of the responders. Google Maps API can also determine city names given the latitude and longitude that we are receiving from the GPS. 



# Getting started / Usage Guide

There is no installation required for this application, as we aim to make it extremely accessible and quick for everyone to utilise, therefore we developed a website based application for both users.

**To get the most out of this application, it is preferable to use both a desktop and mobile at the same time.**

On your mobile, access the responder URL here: <https://scdf-incognito.us-south.cf.appdomain.cloud/responder>

On your desktop, access the SCDF Operator URL here: <https://scdf-incognito.us-south.cf.appdomain.cloud/>

The website dashboard is real-time, and will display changes made by the responders. (Do let us know if you want us to clean the history of the records for recording/demo purposes)

- Step 1 - As a responder, upload a picture of either a car crash accident, or a fire. You may also try to test the machine learning model by uploading a picture of normal traffic / high traffic.

- Step 2 - Submit the photo, it will load for a few seconds before bringing you (the responder) to another page with steps to follow to triage the incident.

- Step 3 - Access the website dashboard as the SCDF Operator. The record of the photo uploaded should reflect on the website. (Refresh if it hasn’t). As the operator, during periods of high traffic, you may choose to prioritise certain incidents with the limited resources by analysing the severity of the incidents using the photos uploaded. The AI model has also given a good prediction of what is the incident about (fire/car accident). 

# Live Demo / Links

Pitch Demo: <>

Website Dashboard: <>

Responder Website: <>

Real-time Car Crash Recognition: <https://youtu.be/0Owg8Iriz28>

# Technologies Used

Current Prototype:

- IBM Cloud Foundry
- Python - Flask
- IBM Visual Recognition
- IBM Language Translator
- IBM Cloudant

Planned Future:

- IBM Text To Speech
- Twilio
