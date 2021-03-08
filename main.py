import hand
import cv2
import gesture
import roi
#import Lights

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
hand = hand.Hand()
roi = roi.roi()
command = 0
fingerCount = 0
lastCount =0
crop=0

while True:
    t, image = cap.read()

    if t :

        try:

            cv2.setMouseCallback('Hands', roi.getroi)
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image = roi.drawSquare(image)
            crop = image

            if roi.isItCropped:

                image = roi.cropimage(image)
                image = hand.gendatadrawhand(image)
                fingerCount = gesture.handData(hand.handLandmarkData, hand.handSide)
                crop[roi.start, roi.finish] = image

            else:
                hand.generatedata(image)
                image = hand.drawhand(image)
                fingerCount = gesture.handData(hand.handLandmarkData, hand.handSide)

        except:
            print("hand not detected")

        try:
            fingerCount = gesture.handData(hand.handLandmarkData, hand.handSide)
        except:
            print("")

        print(fingerCount)

        if fingerCount != lastCount:
            lastCount = fingerCount
            #Lights.lights(fingerCount)
            print("value has  CHANGE")
        else:
            print("value has not change")

        if command == 100:
            del roi
            roi = roi.roi()
        if command == 27 :
            break

        crop = cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('crop', crop)
        cv2.imshow('Hands', image)
        command = cv2.waitKey(100)
