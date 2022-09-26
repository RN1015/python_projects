import pyautogui
import cv2
import mediapipe as mp
import time

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands


tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

hands = mp_hand.Hands(max_num_hands=1)

time.sleep(5)

while True:

    ret, image = video.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    lmList = []
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            myHands = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHands.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])

            mp_draw.draw_landmarks(
                image, hand_landmark,
                mp_hand.HAND_CONNECTIONS)

    fingers = []
    if len(lmList) != 0:
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[4]][1]:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)  # 1 means open
            else:
                fingers.append(0)  # 0 means close

        elif lmList[tipIds[0]][1] < lmList[tipIds[4]][1]:
            if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)  # 1 means open
            else:
                fingers.append(0)  # 0 means close

        # Other four fingers
        
        if lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]:
            fingers.append(1)  # 1 means open
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]:
            fingers.append(1)  # 1 means open
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]:
            fingers.append(1)  # 1 means open
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]:
            fingers.append(1)  # 1 means open
        else:
            fingers.append(0)  # 0 means close

        total = fingers.count(1)

        if total == 0:
            pyautogui.keyUp('left')
            pyautogui.keyDown('right')

        elif total == 2:
            exit()

        elif total == 5:
            pyautogui.keyUp('right')
            pyautogui.keyDown('left')



    if cv2.waitKey(33) == 27:
        break

video.release()
cv2.destroyAllWindows()