from time import sleep
import pyo
import json
import redis


with open('config.json', 'r') as fp:
    config = json.load(fp)

r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()
sf = pyo.SfPlayer("mistergood.wav", loop=True) 
#sh = pyo.FreqShift(sf).out()
hr = pyo.Harmonizer(sf).out()
#ch = pyo.Chorus(sh).out()
dly = pyo.Delay(hr).out()


server.start()

room_temp = r.rpop('temp')
room_mod = (int(room_temp) - 19000) / 1000

while True:
    temp = int(room_temp) - int(r.rpop('temp'))
    if temp is None:
        print("Queue is empty")
        sleep(.1)
    if temp > abs(int(room_temp)+1000):
        print("Currently room temp")
        sleep(.1)
    else:
        print(f'got {temp} on a worker')
        mod = (int(temp) - 19000) / 1000  # range between -14 and 14
        print(f'using mod {mod}')
        hr.transpo = mod - 7
        print(f"set transpo to {hr.transpo}")
        dly.delay = (mod + 14) * 0.05
        print(f"set delay to {dly.delay}")
        #sh.setShift((mod + 14) * 30)
       # print(f"set shift to {sh.shift}")

        #sf.setSpeed((mod+14)/14)
        #print(f"set speed to {sf.speed}")
