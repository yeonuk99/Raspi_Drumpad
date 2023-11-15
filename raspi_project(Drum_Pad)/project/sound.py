import RPi.GPIO as GPIO
import time
import pygame
import threading
from flask import Flask
from flask import render_template
# 초기화
pygame.init() 

# 오디오 초기화
pygame.mixer.init()


app = Flask(__name__)

#오디오 파일 로딩
snare_sample = pygame.mixer.Sound('platesn2.wav')
hihat_sample = pygame.mixer.Sound('close_hi_hat.wav')
bass_sample = pygame.mixer.Sound('bass1.wav')
cymbal_sample = pygame.mixer.Sound('45666__pjcohen__zildjian-a-custom-hi-hat-cymbals-loose-hit.wav')
tomtom_sample = pygame.mixer.Sound('170490__kiddinla__low-floor-tom.wav')


#GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

snare_button = 15
hihat_button = 18
bass_button = 14
cymbal_button = 23
tomtom_button = 24

GPIO.setup(snare_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(hihat_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(bass_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cymbal_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(tomtom_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

snare_channel = pygame.mixer.Channel(0)
hihat_channel = pygame.mixer.Channel(1)
bass_channel = pygame.mixer.Channel(2)
cymbal_channel = pygame.mixer.Channel(3)
tomtom_channel = pygame.mixer.Channel(4)

img_select = ""


@app.route("/")
def make_website():
    img_select = "hihat.jpg"
    return render_template("show_web.html", image_file = img_select)







#콜백 함수
def play_snare(channel):
    try:
        img_select = "snare.jpg"
        threading.Thread(target=play_sound, args = (snare_sample, )).start()
        
        return "snare"
    except:
        return "fail"
    # try:
    #     snare_channel.play(snare_sample)
    #     return "ok"
    # except:
    #     return "fail"



def play_open_kick(channel):
    try:
        img_select = "hihat.jpg"
        threading.Thread(target=play_sound, args = (hihat_sample, )).start()
        return "hihat"
    except:
        return "fail"
    #hihat_channel.play(hihat_sample)


def play_close_kick(channel):
    try:
        img_select = "bass.jpg"
        threading.Thread(target=play_sound, args = (bass_sample, )).start()
        return "bass"
    except:
        return "fail"
    #bass_channel.play(bass_sample)


def play_cymbal(channel):
    try:
        img_select = "cymbal.jpg"
        threading.Thread(target=play_sound, args = (cymbal_sample, )).start()
        return "cymbal"
    except:
        return "fail"
    #cymbal_channel.play(cymbal_sample)
    #cymbal_channel.play(cymbal_sample)


def play_tomtom(channel):
    try:
        img_select = "tom.jpg"
        threading.Thread(target=play_sound, args = (tomtom_sample, )).start()
        return "tomtom"
    except:
        return "fail"
    #tomtom_channel.play(tomtom_sample)

#오디오 출력 함수
@app.route("/play/sound")
def play_sound(sound):

    sound.play()

# GPIO 핀에 이벤트 감지 콜백 함수 연결
GPIO.add_event_detect(snare_button, GPIO.RISING, callback=play_snare, bouncetime = 320)
GPIO.add_event_detect(hihat_button, GPIO.RISING, callback=play_open_kick, bouncetime = 320)
GPIO.add_event_detect(bass_button, GPIO.RISING, callback=play_close_kick, bouncetime = 320)
GPIO.add_event_detect(cymbal_button, GPIO.RISING, callback=play_cymbal, bouncetime = 320)
GPIO.add_event_detect(tomtom_button, GPIO.RISING, callback=play_tomtom, bouncetime = 320)






if __name__ == "__main__":
    app.run(host = "0.0.0.0")


#무한루프
while 1:
    time.sleep(0.1)




# import pygame
# import RPi.GPIO as GPIO
# import threading
# import time

# # 초기화
# pygame.mixer.init()
# GPIO.setmode(GPIO.BCM)

# # 오디오 파일 로딩
# kick_sound = pygame.mixer.Sound('platesn2.wav')
# snare_sound = pygame.mixer.Sound('close_hi_hat.wav')
# hihat_sound = pygame.mixer.Sound('bass1.wav')

# # GPIO 핀 설정
# kick_button = 15
# snare_button = 14
# hihat_button = 18
# buttons = [kick_button, snare_button, hihat_button]

# for button in buttons:
#     GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# # 버튼 상태를 저장하는 딕셔너리 초기화
# button_state = {button: False for button in buttons}

# # 오디오 출력 함수
# def play_sound(sound):
#     sound.play()

# # 버튼 이벤트 처리 함수
# def button_pressed(channel):
#     #if not button_state[channel]:
#     if channel == kick_button:
#         threading.Thread(target=play_sound, args=(kick_sound,)).start()
#     elif channel == snare_button:
#             threading.Thread(target=play_sound, args=(snare_sound,)).start()
#     elif channel == hihat_button:
#         threading.Thread(target=play_sound, args=(hihat_sound,)).start()
        
#         #button_state[channel] = True

# # GPIO 핀에 이벤트 감지 콜백 함수 연결
# for button in buttons:
#     GPIO.add_event_detect(button, GPIO.RISING, callback=button_pressed, bouncetime=150)

# try:
#     while True:
#         pass  # 메인 스레드 계속 실행

# except KeyboardInterrupt:
#     pygame.mixer.quit()
#     GPIO.cleanup()





# import alsaaudio as audio
# import pygame
# import RPi.GPIO as GPIO
# import time
# import threading
# import numpy as np

# audio_lock = threading.Lock()


# # GPIO 핀 설정
# kick_button = 15
# open_hihat_button = 14
# close_hihat_button = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(kick_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(open_hihat_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(close_hihat_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)




# # 오디오 초기화
# pcm = audio.PCM(type=audio.PCM_PLAYBACK, mode=audio.PCM_NORMAL)
# pcm.setformat(audio.PCM_FORMAT_S16_LE)
# pcm.setrate(44100)  # 샘플링 레이트 설정 (원하는 값으로 변경)
# pcm.setchannels(1)  # 스테레오 설정 (1로 변경하면 모노)
# pcm.setperiodsize(1024)  # 오디오 버퍼 크기 설정 (원하는 값으로 변경)



# # 오디오 파일 로딩
# # smaplerate = 44100
# # channels = 1
# # bit = 16
# #type = wav

# kick_sound = open('181321__ojirio__snare.wav', 'rb')
# open_hihat_sound = open('45666__pjcohen__zildjian-a-custom-hi-hat-cymbals-loose-hit.wav', 'rb')
# close_hihat_sound =  open('35634__sandyrb__real-closed-hat-002.wav', 'rb')



# # 버튼 이벤트 처리 함수
# def play_audio1(start_sound):
#     data = start_sound.read(2048)
#     while data:
#         pcm.write(data)
#         data = start_sound.read(2048)
#     start_sound.seek(0)



# def kick(channel):
#     threading.Thread(target=play_audio1, args = (kick_sound, )).start()

# def open_hihat(channel):
#     threading.Thread(target=play_audio1, args = (open_hihat_sound, )).start()

# def close_hihat(channel):
#     threading.Thread(target=play_audio1, args = (close_hihat_sound, )).start()





# # GPIO 핀에 이벤트 감지 콜백 함수 연결
# GPIO.add_event_detect(kick_button, GPIO.RISING, callback=kick, bouncetime=100)
# GPIO.add_event_detect(open_hihat_button, GPIO.RISING, callback=close_hihat, bouncetime=100)
# GPIO.add_event_detect(close_hihat_button, GPIO.RISING, callback=open_hihat, bouncetime=100)

# try:
#     while True:
#         pass  # 메인 스레드 계속 실행

# except KeyboardInterrupt:
#     kick_sound.close()
#     open_hihat_sound.close()
#     close_hihat_sound.close()
#     pcm.close()
#     GPIO.cleanup()














