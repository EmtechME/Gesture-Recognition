import mediapipe as mp


class Hand:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.5, min_tracking_confidence=0.5,max_num_hands=1)
        self.results = 0
        self.image=0
        self.handLandmarkData=0
        self.handSide=0

    def generatedata(self,image):

        self.results = self.hands.process(image)
        try:
            self.handLandmarkData=self.results.multi_hand_landmarks[0].landmark._values
            self.handSide = self.results.multi_handedness[0].classification._values[0].label
        except:
            print("")
    def drawhand(self,image):

        mp_drawing = mp.solutions.drawing_utils
        if self.results.multi_hand_landmarks:
          for hand_landmarks in self.results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
              image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def gendatadrawhand(self,image):

        try:
            self.handLandmarkData=self.results.multi_hand_landmarks[0].landmark._values
            self.handSide = self.results.multi_handedness[0].classification._values[0].label
        except:
            print("")
        self.results = self.hands.process(image)
        mp_drawing = mp.solutions.drawing_utils
        if self.results.multi_hand_landmarks:
          for hand_landmarks in self.results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
              image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return image
