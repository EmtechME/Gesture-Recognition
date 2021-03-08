# Gesture-Recognition

This project is a hand gesture recognition program that recognizes finger counting gestures from 0 to 5 and hand side (left or right), after being recognized it triggers Philips’s hue lights to do commands such as change color of light (applicable is you have colored light bulbs) and to dim or increase the intensity of the lights (0 off - 5 max brightness).


# Prerequisites 
The following libraries are needed in order to run this program.

1 python 3.x
2 mediapie 
3 OpenCV
4 NumPy
5 py2exe

# Run the program

to run the program just download the script and double click on the main.py, otherwise in command prompt got to the directory where you downloaded the script and type python main.py 
the command to control lights is commented, so you can test with out the light and for you to add the IP of your hub.


# Lights.py

here in line 3 of the file you need to add the Ip of your hub.
where you control what does the Philips hue light do and where you can customize 
the light bulbs actions depending on your needs. 

# Hand.py

Here all the information acquired from the frame is processed and returns the location of the hand and it can be use just to extract the information or to draw the skeleton of the hand.

# Gesture.py
 
All the data adquired from Hand.py is processed here , and where it detects which gesture is the hand doing according to the data points received from Hand.py

# roi.py

You can also customize where in the camera frame you want the hand gesture to detect and retreive the information, just by clicking from top right to bottom left. 



