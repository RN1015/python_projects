import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
import requests
import json
from win32com.client import Dispatch
import sys
from tkinter import *
import time
import calendar
from pyautogui import press, typewrite, hotkey
import keyboard

dt = datetime.datetime.now()
engine = pyttsx3.init('sapi5')
# print(voices)
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


client = wolframalpha.Client("5Y6L5H-GLHKJXTYAT")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        speak("Good Morning sir!")
    
    elif hour>=12 and hour<=16:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("How may I help you?")

def takeCommand():
    # Uses Mic

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        # print(e)
        speak(".....")
        return "None"
    return query

hotkey("win", "down")
wishMe()

if __name__ == "__main__":
    
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
            input()

        elif 'open' in query:
            if 'google' in query or 'chrome' in query:
                speak("Opening Google")
                webbrowser.open("google.com")
                input()

            elif 'youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("youtube.com")
                input()
            
            else:
                hotkey('win')
                prgrm = query.replace('open', '')
                typewrite(prgrm)
                hotkey('enter')

        elif 'good morning' in query or 'good afternoon' in query or 'good afternoon' in query:
            print(":)")
        
        elif 'shutdown' in query:
            speak("Shutting down")
            hotkey('win', 'm')
            keyboard.press_and_release('enter')
            hotkey('alt', 'f4')
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
        
        elif 'exit' in query or 'flip' in query or 'sleep' in query or 'nothing' in query or 'not to you' in query or 'bye' in query or 'good night' in query:
            exit()

        elif 'detect object' in query or 'detect objects' in query:
            # opencv object tracking
            # object detection and tracking opencv
            import cv2
            import numpy as np
            
            # Load Yolo
            yolo_weight = "yolov3.weights"
            yolo_config = "yolov3.cfg.txt"
            coco_labels = "coco.names.txt"
            net = cv2.dnn.readNet(yolo_weight, yolo_config)
            classes = []
            with open(coco_labels, "r") as f:
                classes = [line.strip() for line in f.readlines()]
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            # Defining desired shape
            fWidth = 256
            fHeight = 256
            
            # Below function will read video frames
            cap = cv2.VideoCapture(0)
            
            while True:
                read_ok, img = cap.read()
            
                height, width, channels = img.shape
            
                # Detecting objects
                blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                net.setInput(blob)
                outs = net.forward(output_layers)
            
                # Showing informations on the screen
                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            # Object detected
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)
                            # Rectangle coordinates
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)
                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)
            
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            
                font = cv2.FONT_HERSHEY_DUPLEX
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        confidence_label = int(confidences[i] * 100)
                        alpha = str(confidence_label) + '%'
                        color = colors[i]
                        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(img, f'{label, alpha}', (x-25, y + 75), font, 2, color, 2)
            
                cv2.imshow("Image", img)
                # Close video window by pressing Enter
                if cv2.waitKey(33) == 13:
                    break

        elif 'detect finger' in query or 'detect number of fingers' in query:
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
        
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            App = "C:\\Users\\T.V.M.RAYUDU\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(App)
            input()

        elif 'system info' in query or 'system information' in query:
            speak('fetching your current system info...')
            import psutil
            import platform
            from datetime import datetime
            def get_size(bytes, suffix="B"):
                """
                Scale bytes to its proper format
                e.g:
                    1253656 => '1.20MB'
                    1253656678 => '1.17GB'
                """
                factor = 1024
                for unit in ["", "K", "M", "G", "T", "P"]:
                    if bytes < factor:
                        return f"{bytes:.2f}{unit}{suffix}"
                    bytes /= factor
            print("="*40, "System Information", "="*40)
            uname = platform.uname()
            print(f"System: {uname.system}")
            print(f"Node Name: {uname.node}")
            print(f"Release: {uname.release}")
            print(f"Version: {uname.version}")
            print(f"Machine: {uname.machine}")
            print(f"Processor: {uname.processor}")
            # Boot Time
            print("="*45, "Boot Time", "="*44)
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
            # let's print CPU information
            print("="*45, "CPU Info", "="*45)
            # number of cores
            print("Physical cores:", psutil.cpu_count(logical=False))
            print("Total cores:", psutil.cpu_count(logical=True))
            # CPU frequencies
            cpufreq = psutil.cpu_freq()
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
            # CPU usage
            print("CPU Usage Per Core:")
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {percentage}%")
            print(f"Total CPU Usage: {psutil.cpu_percent()}%")
            # Memory Information
            print("="*40, "Memory Information", "="*40)
            # get the memory details
            svmem = psutil.virtual_memory()
            print(f"Total: {get_size(svmem.total)}")
            print(f"Available: {get_size(svmem.available)}")
            print(f"Used: {get_size(svmem.used)}")
            print(f"Percentage: {svmem.percent}%")
            print("="*47, "SWAP", "="*47)
            # get the swap memory details (if exists)
            swap = psutil.swap_memory()
            print(f"Total: {get_size(swap.total)}")
            print(f"Free: {get_size(swap.free)}")
            print(f"Used: {get_size(swap.used)}")
            print(f"Percentage: {swap.percent}%")
            # Disk Information
            print("="*41, "Disk Information", "="*41)
            print("Partitions and Usage:")
            # get all disk partitions
            partitions = psutil.disk_partitions()
            for partition in partitions:
                print(f"=== Device: {partition.device} ===")
                print(f"  Mountpoint: {partition.mountpoint}")
                print(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    # this can be catched due to the disk that
                    # isn't ready
                    continue
                print(f"  Total Size: {get_size(partition_usage.total)}")
                print(f"  Used: {get_size(partition_usage.used)}")
                print(f"  Free: {get_size(partition_usage.free)}")
                print(f"  Percentage: {partition_usage.percent}%")
            # get IO statistics since boot
            disk_io = psutil.disk_io_counters()
            print(f"Total read: {get_size(disk_io.read_bytes)}")
            # Network information
            print("="*40, "Network Information", "="*40)
            # get all network interfaces (virtual and physical)
            if_addrs = psutil.net_if_addrs()
            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    print(f"=== Interface: {interface_name} ===")
                    if str(address.family) == 'AddressFamily.AF_INET':
                        print(f"  IP Address: {address.address}")
                        print(f"  Netmask: {address.netmask}")
                        print(f"  Broadcast IP: {address.broadcast}")
                    elif str(address.family) == 'AddressFamily.AF_PACKET':
                        print(f"  MAC Address: {address.address}")
                        print(f"  Netmask: {address.netmask}")
                        print(f"  Broadcast MAC: {address.broadcast}")
            # get IO statistics since boot
            net_io = psutil.net_io_counters()
            print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
            print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
            input()
        
        elif 'your info' in query or 'who are you' in query:
            print("I am R-Nutro, a computer program created through python via VS code by mister TVMRayudu. My Python Verson...3.8.6; 64-bit, on a WINDOWS 10 OS")
            speak("I am R-Nutro, a computer program created through python via VS code by mister TVMRayudu. My Python Verson...3.8.6; 64-bit, on a WINDOWS 10 OS")

        elif 'where is' in query:
            plc = query.split(" ")
            location = plc[2]
            webbrowser.open("https://www.google.nl/maps/place/" + location)
            input()

        elif 'remember' in query:
            mmr = query.replace("remember", "")
            speak("remembered")

        elif 'what i told you to remember' in query or 'what did i tell you to remember' in query or 'where did i keep my' in query:
            speak('you said the following sentence: ' + mmr)
            print(mmr)
        
        elif 'weather forecast' in query:
            speak("Searching...")
            res = client.query(query)
            results = next(res.results).text
            print(results)
            speak(results)

        elif 'news' in query:
            speak("Searching")
            speak("News for today")
            url = 'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=3686d5d7b2b546f0a7654515df0932b7'
            news = requests.get(url).text
            news_dict = json.loads(news)
            print(news_dict["articles"])
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                speak("                          ")
                input()

        elif 'good' in query or 'nice' in query:
            speak("Thank You sir")

        elif 'thank you' in query or 'thanks' in query:
            speak("You're Welcome!")

        elif 'stopwatch' in query:
            speak('Starting Stopwatch')
            def time_convert(sec):
                mins = sec // 60
                sec = sec % 60
                hours = mins // 60
                mins = mins % 60
                print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

            speak('Press Enter to start')
            input("Press Enter to start")
            start_time = time.time()

            speak('Press Enter to stop')
            input("Press Enter to stop")
            end_time = time.time()

            time_lapsed = end_time - start_time
            time_convert(time_lapsed)


        elif 'desktop' in query or 'minimise' in query or 'home' in query:
            hotkey('win', 'm')
            input()

        elif 'check this website' in query:
            import urlexpander
            b = input("Ener URL: ")
            if 'https://' in b:
                pass
            else:
                b = 'https://www.' + b
            a = urlexpander.expand(b)
            if 'loclx' in a or 'ngrock' in a or 'sttp' in a:
                print("STOP!!! This might harm your privacy")
            else:
                print("This is probably safe")

            x = input()

        elif 'game' in query or 'play' in query:
            # Tic Tac Toe

            import random

            def drawBoard(board):
                # "board" is a list of 10 strings representing the board (ignore index 0)
                print('       |       |')
                print(' ' + board[7] + '     | ' + board[8] + '     | ' + board[9])
                print('       |       |')
                print('-------+-------+-------')
                print('       |       |')
                print(' ' + board[4] + '     | ' + board[5] + '     | ' + board[6])
                print('       |       |')
                print('-------+-------+-------')
                print('       |       |')
                print(' ' + board[1] + '     | ' + board[2] + '     | ' + board[3])
                print('       |       |')

            def inputPlayerLetter():
                # Let's the player type which letter they want to be.
                # Returns a list with the player's letter as the first item, and the computer's letter as the second.
                letter = ''
                while not (letter == 'X' or letter == 'O'):
                    print('Do you want to be X or O?')
                    letter = input().upper()

                # the first element in the tuple is the player's letter, the second is the computer's letter.
                if letter == 'X':
                    return ['X', 'O']
                else:
                    return ['O', 'X']

            def whoGoesFirst():
                # Randomly choose the player who goes first.
                if random.randint(0, 1) == 0:
                    return 'I'
                else:
                    return 'You'

            def playAgain():
                # This function returns True if the player wants to play again, otherwise it returns False.
                print('Do you want to play again? (yes or no)')
                speak('Do you want to play again? (yes or no)')
                return input().lower().startswith('y')

            def makeMove(board, letter, move):
                board[move] = letter

            def isWinner(bo, le):
                # Given a board and a player's letter, this function returns True if that player has won.
                # We use bo instead of board and le instead of letter so we don't have to type as much.
                return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

            def getBoardCopy(board):
                # Make a duplicate of the board list and return it the duplicate.
                dupeBoard = []

                for i in board:
                    dupeBoard.append(i)

                return dupeBoard

            def isSpaceFree(board, move):
                # Return true if the passed move is free on the passed board.
                return board[move] == ' '

            def getPlayerMove(board):
                # Let the player type in his move.
                move = ' '
                while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
                    print('What is your next move? (1-9)')
                    speak('Your turn sir')
                    move = input()
                return int(move)

            def chooseRandomMoveFromList(board, movesList):
                # Returns a valid move from the passed list on the passed board.
                # Returns None if there is no valid move.
                possibleMoves = []
                for i in movesList:
                    if isSpaceFree(board, i):
                        possibleMoves.append(i)

                if len(possibleMoves) != 0:
                    return random.choice(possibleMoves)
                else:
                    return None

            def getComputerMove(board, computerLetter):
                # Given a board and the computer's letter, determine where to move and return that move.
                if computerLetter == 'X':
                    playerLetter = 'O'
                else:
                    playerLetter = 'X'

                # Here is our algorithm for our Tic Tac Toe AI:
                # First, check if we can win in the next move
                for i in range(1, 10):
                    copy = getBoardCopy(board)
                    if isSpaceFree(copy, i):
                        makeMove(copy, computerLetter, i)
                        if isWinner(copy, computerLetter):
                            return i

                # Check if the player could win on his next move, and block them.
                for i in range(1, 10):
                    copy = getBoardCopy(board)
                    if isSpaceFree(copy, i):
                        makeMove(copy, playerLetter, i)
                        if isWinner(copy, playerLetter):
                            return i

                # Try to take one of the corners, if they are free.
                move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
                if move != None:
                    return move

                # Try to take the center, if it is free.
                if isSpaceFree(board, 5):
                    return 5

                # Move on one of the sides.
                return chooseRandomMoveFromList(board, [2, 4, 6, 8])

            def isBoardFull(board):
                # Return True if every space on the board has been taken. Otherwise return False.
                for i in range(1, 10):
                    if isSpaceFree(board, i):
                        return False
                return True


            print('Welcome to Tic Tac Toe!')
            speak('Welcome to Tic Tac Toe!')
            speak('Instructions')
            print('''Instructions: 
                        7 8 9
                        4 5 6
                        1 2 3''')

            while True:
                # Reset the board
                theBoard = [' '] * 10
                playerLetter, computerLetter = inputPlayerLetter()
                turn = whoGoesFirst()
                trn = print(turn + ' will go first.')
                trn
                if trn == "I will go first.":
                    speak('My turn')
                gameIsPlaying = True

                while gameIsPlaying:
                    if turn == 'You':
                        # Player's turn.
                        drawBoard(theBoard)
                        move = getPlayerMove(theBoard)
                        makeMove(theBoard, playerLetter, move)

                        if isWinner(theBoard, playerLetter):
                            drawBoard(theBoard)
                            print('Hurray! You have won the game!')
                            speak('Congratulations!!')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game was a tie!')
                                speak('The game was a tie!')
                                break
                            else:
                                turn = 'I'

                    else:
                        # Computer's turn.
                        move = getComputerMove(theBoard, computerLetter)
                        makeMove(theBoard, computerLetter, move)

                        if isWinner(theBoard, computerLetter):
                            drawBoard(theBoard)
                            print('I Won')
                            speak('I Won')
                            gameIsPlaying = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('The game was a tie!')
                                speak('The game was a tie!')
                                break
                            else:
                                turn = 'You'

                if not playAgain():
                    break

        else:
            try:
                print(".....")
                res = client.query(query)
                results = next(res.results).text
                if results == '''1 | noun | a canonical hour that is the ninth hour of the day counting from sunrise
2 | noun | a service in the Roman Catholic Church formerly read or chanted at 3 PM (the ninth hour counting from sunrise) but now somewhat earlier
3 | adjective | not any
4 | adverb | not at all or in no way
5 | pronoun | not one, not any; no one, nobody; nothing, no part
(5 meanings)''':
                    speak(".....")
                
                else:
                    print(results)
                    speak(results)

            except:
                hotkey('win')
                typewrite(query)
                speak('Here are some matching results')
                input()