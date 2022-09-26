import cv2
import mediapipe as mp
import time

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands


tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

hands = mp_hand.Hands(max_num_hands=1)

pTime = 0

while True:
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

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
                cv2.putText(image, "True", (150, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            else:
                fingers.append(0)  # 0 means close

        elif lmList[tipIds[0]][1] < lmList[tipIds[4]][1]:
            if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)  # 1 means open
                cv2.putText(image, "True", (150, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            else:
                fingers.append(0)  # 0 means close

        # Other four fingers
        
        if lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2]:
            fingers.append(1)  # 1 means open
            cv2.putText(image, "True", (150, 80), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2]:
            fingers.append(1)  # 1 means open
            cv2.putText(image, "True", (150, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2]:
            fingers.append(1)  # 1 means open
            cv2.putText(image, "True", (150, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        else:
            fingers.append(0)  # 0 means close

        if lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2]:
            fingers.append(1)  # 1 means open
            cv2.putText(image, "True", (150, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        else:
            fingers.append(0)  # 0 means close

        total = fingers.count(1)

        if total == 0:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "0", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 15)

        elif total == 1:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "1", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (225, 0, 0), 15)

        elif total == 2:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "2", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (225, 0, 0), 15)

        elif total == 3:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "3", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (225, 0, 0), 15)

        elif total == 4:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "4", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (225, 0, 0), 15)

        elif total == 5:
            cv2.rectangle(image, (15, 225), (135, 375), (0, 225, 0), -1)
            cv2.putText(image, "5", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (225, 0, 0), 15)

        

    cv2.putText(image, f'FPS: {int(fps)}', (45, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.putText(image, "Thumb Finger:", (25, 40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.putText(image, "Index Finger:", (25, 80), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.putText(image, "Middle Finger:", (25, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.putText(image, "Ring Finger:", (25, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.putText(image, "Little Finger:", (25, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    cv2.imshow("Finger Counter", image)



    if cv2.waitKey(33) == 13:
        break

video.release()
cv2.destroyAllWindows()