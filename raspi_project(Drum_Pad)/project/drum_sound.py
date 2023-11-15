import RPi.GPIO as GPIO
import pygame
import threading
from pygame.locals import *


# 초기화
pygame.init() 

# 오디오 초기화
pygame.mixer.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame drumpad screen")

#이미지 파일 로딩

background = pygame.image.load("consert_img.jpg")

# 드럼 사운드1
img_snare = pygame.image.load("basic_snare1.jpg")
img_hihat = pygame.image.load("basic_hihat.jpg")
img_bass = pygame.image.load("basic_bass.jpg")
img_tom = pygame.image.load("basic_tomtom.jpg")
img_cymbal = pygame.image.load("basic_cymbal.jpg")

# 드럼 사운드2
img_EDM_snare = pygame.image.load("EDM_snare_img.jpg")
img_EDM_hihat = pygame.image.load("EDM_hihat_img.jpg")
img_EDM_bass = pygame.image.load("EDM_bass_img.jpg")
img_EDM_cymbal = pygame.image.load("EDM_cymbal_img.jpg")
img_clap = pygame.image.load("edm_clap.jpg")





#오디오 파일 로딩
# 드럼 사운드1
snare_sample = pygame.mixer.Sound('basic_snare.wav')
hihat_sample = pygame.mixer.Sound('basic_hihat.wav')
bass_sample = pygame.mixer.Sound('basic_bass.wav')
cymbal_sample = pygame.mixer.Sound('basic_cymbal.wav')
tomtom_sample = pygame.mixer.Sound('basic_tomtom.wav')

# 드럼 사운드2
edm_snare_sample = pygame.mixer.Sound('673492__theendofacycle__edm-snare-drum.wav')
edm_hihat_sample = pygame.mixer.Sound('EDM_hihat.wav')
edm_bass_sample = pygame.mixer.Sound('EDM_kick.wav')
edm_cymbal_sample = pygame.mixer.Sound('382967__insintesi__syn-bass-drum-6.wav')
edm_tomtom_sample = pygame.mixer.Sound('336657__hard3eat__clap-07.wav')



#GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

snare_button = 15
hihat_button = 18
bass_button = 14
cymbal_button = 23
tomtom_button = 24
change_button = 25

GPIO.setup(snare_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(hihat_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(bass_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cymbal_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(tomtom_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(change_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# snare_channel = pygame.mixer.Channel(0)
# hihat_channel = pygame.mixer.Channel(1)
# bass_channel = pygame.mixer.Channel(2)
# cymbal_channel = pygame.mixer.Channel(3)
# tomtom_channel = pygame.mixer.Channel(4)

global img_select
img_select = ""

global change_percussion
change_percussion = True


# 이미지 위치 설정
image_x = (screen_width - img_EDM_snare.get_width()) // 2
image_y = (screen_height - img_EDM_snare.get_height()) // 2

#콜백 함수
def change_Sound(channel):
    global change_percussion
    if change_percussion == True:
        change_percussion = False
        print("True")
    elif change_percussion == False:
        change_percussion = True
        print("False")
    


def play_snare(channel):
    try:
        global img_select
        if change_percussion == True:
            img_select = "snare.jpg"
            threading.Thread(target=play_sound, args = (snare_sample, )).start()  
        elif change_percussion == False:
            img_select = "EDM_snare_img.jpg"
            threading.Thread(target=play_sound, args = (edm_snare_sample, )).start()
    except:
        print("Fail")

def play_hihat(channel):
    try:
        global img_select
        if change_percussion == True:
            img_select = "hihat.jpg"
            threading.Thread(target=play_sound, args = (hihat_sample, )).start()
        elif change_percussion == False:
            img_select = "EDM_hihat_img.jpg"
            threading.Thread(target=play_sound, args = (edm_hihat_sample, )).start()  
        
    except:
        return "fail"



def play_bass(channel):
    try:
        global img_select
        if change_percussion == True:
            img_select = "bass.jpg"
            threading.Thread(target=play_sound, args = (bass_sample, )).start()
        elif change_percussion == False:
            img_select = "EDM_bass_img.jpg"
            threading.Thread(target=play_sound, args = (edm_bass_sample, )).start()
        
    except:
        return "fail"



def play_cymbal(channel):
    try:
        global img_select
        if change_percussion == True:
            img_select = "cymbal.jpg"
            threading.Thread(target=play_sound, args = (cymbal_sample, )).start()
        elif change_percussion == False:
            img_select = "EDM_cymbal_img.jpg"
            threading.Thread(target=play_sound, args = (edm_cymbal_sample, )).start()
    except:
        return "fail"
        

def play_tomtom(channel):
    try:
        global img_select
        
        if change_percussion == True:
            img_select = "tom.jpg"
            threading.Thread(target=play_sound, args = (tomtom_sample, )).start()
        elif change_percussion == False:
            img_select = "clap.jpg"
            threading.Thread(target=play_sound, args = (edm_tomtom_sample, )).start()
        
    except:
        return "fail"

#오디오 출력 함수
def play_sound(sound):
    sound.play()






# GPIO 핀에 이벤트 감지 콜백 함수 연결
GPIO.add_event_detect(snare_button, GPIO.RISING, callback=play_snare, bouncetime = 320)
GPIO.add_event_detect(hihat_button, GPIO.RISING, callback=play_hihat, bouncetime = 320)
GPIO.add_event_detect(bass_button, GPIO.RISING, callback=play_bass, bouncetime = 320)
GPIO.add_event_detect(cymbal_button, GPIO.RISING, callback=play_cymbal, bouncetime = 320)
GPIO.add_event_detect(tomtom_button, GPIO.RISING, callback=play_tomtom, bouncetime = 320)
GPIO.add_event_detect(change_button, GPIO.RISING, callback=change_Sound, bouncetime = 320)





# 게임 루프
running = True
while running:


    for event in pygame.event.get():
        if event.type == 27:
            running = False

    # 화면을 흰색으로 채우기
    screen.fill((255, 255, 255))

    # 이미지 그리기
    screen.blit(background, (0,0))
    
    if img_select == "snare.jpg":
        screen.blit(img_snare, (image_x, image_y))
    elif img_select == "bass.jpg":
        screen.blit(img_bass, (image_x, image_y))
    elif img_select == "hihat.jpg":
        screen.blit(img_hihat, (image_x, image_y))
    elif img_select == "cymbal.jpg":
        screen.blit(img_cymbal, (image_x, image_y))
    elif img_select == "tom.jpg":
        screen.blit(img_tom, (image_x, image_y))
    elif img_select == "EDM_snare_img.jpg":
        screen.blit(img_EDM_snare, (image_x, image_y))
    elif img_select == "EDM_hihat_img.jpg":
        screen.blit(img_EDM_hihat, (image_x, image_y))
    elif img_select == "EDM_bass_img.jpg":
        screen.blit(img_EDM_bass, (image_x, image_y))
    elif img_select == "EDM_cymbal_img.jpg":
        screen.blit(img_EDM_cymbal, (image_x, image_y))
    elif img_select == "clap.jpg":
        screen.blit(img_clap, (image_x, image_y))
    pygame.display.flip()

    # 화면 업데이트
    pygame.display.update()




