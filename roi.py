import cv2


class roi:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.start = [0]
        self.finish = [0]
        self.firstSelectedFrame = 0
        self.isItCropped = 0

    def getroi (self,action,x,y,flags,user):

        if action == cv2.EVENT_LBUTTONDOWN:
            self.start =(0,0)
            self.start =(x,y)
            print (self.start,"start")

        elif action == cv2.EVENT_LBUTTONUP:
            self.finish = (0,0)
            self.finish = (x, y)
            self.firstSelectedFrame = 1
            if self.finish[0] < self.start[0]:
                self.start = [0]
                self.finish = [0]
                print("values not valids")
            if self.finish[1] < self.start[1]:
                self.start = [0]
                self.finish = [0]
                print("values not valids")

    def drawSquare (self , image):
        try:
            self.image = cv2.rectangle(image, self.start, self.finish, (0,255,0), 3)
            self.isItCropped = 1
        except:
            print("Values for drawing a square not insterted yet")
        return image

    def cropimage (self , image):

        try:
            crop = image [self.start[1]:self.finish[1] , self.start[0]:self.finish[0]]

            return crop
        except:
            print("not croped")

