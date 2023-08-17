import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis! Sir,Please tell me how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please..")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='D:\\songs'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Aman! Sir! ,The Time is {strTime}")
            print(strTime)
        elif 'open spotify' in query:
            spo="C:\\Users\\amssr\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spo)
        elif 'achieve' in query:
            sp="C:\\Users\\amssr\\Desktop\\certificate\\amnisro.pdf"
            os.startfile(sp)
        elif 'system' in query:
            speak('Elvish! yadav! is great! vote for him')
        elif 'shubham' in query:
            speak('sir! sorry! but you are not great! please collect some mind from other great people like aman! sir!')
        elif 'aman' in query:
            speak('Hi! aman! sir! you are great ! you are smart like albert! einstien')
        elif 'mouse control' in query:
            import cv2
            import mediapipe as mp
            import pyautogui

            cam = cv2.VideoCapture(0)
            face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
            screen_w, screen_h = pyautogui.size()
            while True:
                _, frame = cam.read()
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output = face_mesh.process(rgb_frame)
                landmark_points = output.multi_face_landmarks
                frame_h, frame_w, _ = frame.shape
                if landmark_points:
                    landmarks = landmark_points[0].landmark
                    for id, landmark in enumerate(landmarks[474:478]):
                        x = int(landmark.x * frame_w)
                        y = int(landmark.y * frame_h)
                        cv2.circle(frame, (x, y), 3, (0, 255, 0))
                        if id == 1:
                            screen_x = screen_w / frame_w * x
                            screen_y = screen_h / frame_h * y
                            pyautogui.moveTo(screen_x, screen_y)
                    left = [landmarks[145], landmarks[159]]
                    for landmark in left:
                        x = int(landmark.x * frame_w)
                        y = int(landmark.y * frame_h)
                        cv2.circle(frame, (x, y), 3, (0, 255, 255))
                    if (left[0].y - left[1].y) < 0.004:
                        pyautogui.click()
                        # pyautogui.sleep()

                cv2.imshow('Eye Controlled Mouse', frame)
                cv2.waitKey(1)
        elif "horror" in query:
            import pygame
            from time import sleep

            pygame.init()
            window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            pygame.mixer.init()
            pygame.mixer.music.load('ratsasan.mp3')
            pygame.mixer.music.play()
            sleep(5)
            pygame.mixer.music.load('scary.mp3')
            pygame.mixer.music.play()
            sleep(1)
            image = pygame.image.load('scr.jpg')
            window.blit(image, (0, 0))
            pygame.display.update()
            sleep(3)
            pygame.quit()
        elif 'quit' in query:
            speak('bye bye! aman! sir! see you soon')
            break
        else:
            pass

