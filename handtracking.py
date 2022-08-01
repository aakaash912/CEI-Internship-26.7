import cv2
import pyfirmata
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
mp_draw = mp.solutions.drawing_utils
mp_hand=mp.solutions.hands
cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8, maxHands=2)
red1LED=8
red2LED=9
red3LED=10
red4LED=11
red5LED=12
yellow1LED=3
yellow2LED=4
yellow3LED=5
yellow4LED=6
yellow5LED=7
on=1
off=0
board=pyfirmata.Arduino('COM5')
while True:
    success,img=cap.read()
    hands,img=detector.findHands(img)
    if hands:
        hand1=hands[0]
        handType1=hand1["type"]
        if True:
            a=handType1
            if (a == "Right"):
                board.digital[red1LED].write(on)
                board.digital[red2LED].write(on)
                board.digital[red3LED].write(on)
                board.digital[red4LED].write(on)
                board.digital[red5LED].write(on)
                board.digital[yellow1LED].write(off)
                board.digital[yellow2LED].write(off)
                board.digital[yellow3LED].write(off)
                board.digital[yellow4LED].write(off)
                board.digital[yellow5LED].write(off)
            elif (a == "Left"):
                board.digital[red1LED].write(off)
                board.digital[red2LED].write(off)
                board.digital[red3LED].write(off)
                board.digital[red4LED].write(off)
                board.digital[red5LED].write(off)
                board.digital[yellow1LED].write(on)
                board.digital[yellow2LED].write(on)
                board.digital[yellow3LED].write(on)
                board.digital[yellow4LED].write(on)
                board.digital[yellow5LED].write(on)
        if len(hands)==2:
            hand2=hands[1]
            handType2=hand2["type"]
            board.digital[red1LED].write(on)
            board.digital[red2LED].write(on)
            board.digital[red3LED].write(on)
            board.digital[red4LED].write(on)
            board.digital[red5LED].write(on)
            board.digital[yellow1LED].write(on)
            board.digital[yellow2LED].write(on)
            board.digital[yellow3LED].write(on)
            board.digital[yellow4LED].write(on)
            board.digital[yellow5LED].write(on)
    if len(hands) == 0:
        board.digital[red1LED].write(off)
        board.digital[red2LED].write(off)
        board.digital[red3LED].write(off)
        board.digital[red4LED].write(off)
        board.digital[red5LED].write(off)
        board.digital[yellow1LED].write(off)
        board.digital[yellow2LED].write(off)
        board.digital[yellow3LED].write(off)
        board.digital[yellow4LED].write(off)
        board.digital[yellow5LED].write(off)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






