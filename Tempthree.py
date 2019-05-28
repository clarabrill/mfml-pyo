from time import sleep
import pyo
import json
import redis


with open('config.json', 'r') as fp:
    config = json.load(fp)

r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()
sf = pyo.SfPlayer("campersongs/mistergood.wav", loop=True)  
#fs = pyo.FreqShift(sf).out()
#hr = pyo.Harmonizer(sf).out()
#ch = pyo.Chorus(sf).out()
#dly = pyo.Delay(sf).out()

server.gui(locals())

server.start()

# r.lpush goes to r.rpop
# to keep it all organized, have queue
# queue expands and contracts as data comes in per time cycle 
# while True is infinite loop (do forever)

#room_temp is a constant, which is the first temperature 
#temp_diff calibrates first temperature as zero

room_temp = None
while True:
    temp = r.rpop('temp')
    if temp is None:
        print("Queue is empty")
        sleep(.1)
    else:
        print(f'got {temp} on a worker')
        if room_temp is None:
            room_temp = int(temp)

        temp_diff = int(temp) - room_temp 
        print(f'using temp_diff {temp_diff}')

        # Chorus
        # nameofobject.nameoffunction
        # input, depth, feedback, bal=0.5, mul=1, add=0
        # make single reading of first_temp
        # then subtract mod_temp from itself/first_temp
        # formula that maps range of temps to range of depth etc.
        ch.depth = temp_diff 
        print(f"set depth to {ch.depth}")

        # Harmonizer
        # hr_diff = POSITIVE -> NEGATIVE?
        # hr.transpo = 
        #print(f"set transpo to {hr.transpo}")
        # default -7

        # Delay
        #dly_diff = str(mod_temp - 0.25)
        #dly.delay = mod_temp - int(dly_diff)
        #print(f"set delay to {dly.delay}")

        # FreqShift
        #mod_temp_sh = mod_temp * 1000
        #sh_diff = str(mod_temp_sh - 100)
        #sh.setShift(mod_temp_sh - int(sh_diff))
        #print(f"set shift to {sh.shift}")

        #speed_diff = str(mod_temp - 1)
        #sf.setSpeed(mod_temp - int(speed_diff))
        #print(f"set speed to {sf.speed}")
        # defaults to 1

