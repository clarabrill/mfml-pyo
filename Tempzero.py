from time import sleep
import pyo
import json
import redis


with open('config.json', 'r') as fp:
    config = json.load(fp)

r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()
sf = pyo.SfPlayer("mistergood.wav", loop=True)  # .out()?
#fs = FreqShift(sf).out()
#hr = pyo.Harmonizer(sf).out()
ch = pyo.Chorus(sf).out()
dly = pyo.Delay(sf).out()

server.gui(locals())

server.start()


while True:
    temp = r.rpop('temp')
    if temp is None:
        print("Queue is empty")
        sleep(.1)
    else:
        print(f'got {temp} on a worker')

        mod_temp = int(temp) / 80000
        print(f'using mod_temp {mod_temp}')

        # How to only use initial mod_temp for _diff if string doesn't stop it from updating
        
        # Chorus
        ch_diff = str(mod_temp - 1)
        ch.depth = mod_temp - int(ch_diff)
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

