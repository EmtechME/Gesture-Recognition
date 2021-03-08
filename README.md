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


# Lights.py

where you control what does the Philips hue light do and where you can customize 
the light bulbs actions depending on your needs

# Hand.py

Here all the information acquired from the frame is processed and returns the location of the hand and it can be use just to extract the information or to draw the skeleton of the hand.

# Gesture.py

