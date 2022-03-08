#Healthy programmer
# water-watwe.mp3 3.5 liter - Drank -log-every 30 min
# Eye -- eye.mp3 every 30min - eyedone- log log -- every 30 min
# physicsl actavity- physical.mp3 every-45 min- ex done
# rule
# pygame module to play

from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a== stopper:
            mixer.music.stop()

            break
def log_now(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg}  {datetime.now()}\n")



if __name__ == '__main__':
     #musiconloop("mahadev.mp3","stop")
     init_water=time()
     init_eyes=time()
     init_exercise=time()
     watersecs=2*60
     exses=4*60
     eyeses=1*60

     while True:
         if time()- init_water>watersecs:
             print("Water drinking time . Enter 'drank' to stop the alarm")
             musiconloop("mahadev.mp3",'drank')
             init_water = time()
             log_now("Drank water at")
         if time()- init_exercise>exses:
             print("Physicl Excise  time . Enter 'done' to stop the alarm")
             musiconloop("mahadev.mp3",'done')
             init_exercise = time()
             log_now("Physical Exercise done at")
         if time()- init_eyes>eyeses:
             print("Eye  exercise time . Enter 'done' to stop the alarm")
             musiconloop("mahadev.mp3",'done')
             init_eyes = time()
             log_now("Eye relaxed at")






