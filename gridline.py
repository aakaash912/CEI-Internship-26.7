import cv2
import numpy as np
import mediapipe as mp
import pyfirmata

board=pyfirmata.Arduino("COM5")
led1=board.get_pin('d:2:o')
led2=board.get_pin('d:3:o')
led3=board.get_pin('d:4:o')
led4=board.get_pin('d:5:o')
led5=board.get_pin('d:6:o')
led6=board.get_pin('d:7:o')
led7=board.get_pin('d:8:o')
led8=board.get_pin('d:9:o')
led9=board.get_pin('d:10:o')
on=1
off=0
mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

video=cv2.VideoCapture(0)
video.open(0,cv2.CAP_DSHOW)
with mp_hand.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.8,max_num_hands=1,) as hands:
    while True:
        ret,image=video.read()
        image=cv2.flip(image,1)
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB,)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                    if id==8:
                        if 0<=cx<=213:
                            if 0<=cy<=160:
                                board.digital[led1].write(on)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                            elif 161<=cy<=320:
                                board.digital[led1].write(off)
                                board.digital[led2].write(on)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                            elif 321 <= cy <= 480:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(on)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                        elif 214<=cx<=427:
                            if 0<=cy<=160:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(on)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                            elif 161<=cy<=320:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(on)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                            elif 321 <= cy <= 480:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(on)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                        elif 428<=cx<=640:
                            if 0<=cy<=160:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(on)
                                board.digital[led8].write(off)
                                board.digital[led9].write(off)
                            elif 161<=cy<=320:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(on)
                                board.digital[led9].write(off)
                            elif 321 <= cy <= 480:
                                board.digital[led1].write(off)
                                board.digital[led2].write(off)
                                board.digital[led3].write(off)
                                board.digital[led4].write(off)
                                board.digital[led5].write(off)
                                board.digital[led6].write(off)
                                board.digital[led7].write(off)
                                board.digital[led8].write(off)
                                board.digital[led9].write(on)
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        def draw_grid(image, grid_shape, color=(0, 0, 0), thickness=1):
            h, w, _ = image.shape
            rows, cols = grid_shape
            dy, dx = h / rows, w / cols
            # draw vertical lines
            for x in np.linspace(start=dx, stop=w - dx, num=cols - 1):
                x = int(round(x))
                cv2.line(image, (x, 0), (x, h), color=color, thickness=thickness)

            # draw horizontal lines
            for y in np.linspace(start=dy, stop=h - dy, num=rows - 1):
                y = int(round(y))
                cv2.line(image, (0, y), (w, y), color=color, thickness=thickness)

            return image

        draw_grid(image, grid_shape=(3,3))
        cv2.imshow("Video", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
