from time import sleep
import pyo
import json
import redis


with open('config.json', 'r') as fp:
    config = json.load(fp)

r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()

sf = pyo.SfPlayer("campersongs/primarycolors.wav", loop=True)  
sm = pyo.SmoothDelay(sf).out()

server.start()

room_temp = None
while True:
    temp = r.rpop('temp')
    if temp is None:
        print("Queue is empty")
        sleep(1)

    else:
        print(f'got {temp} on a worker')
        if room_temp is None:
            room_temp = int(temp)

        temp_diff = abs(int(temp)  - room_temp) / 10000
        print(f'using temp_diff {temp_diff}')

        #sm.mul = 1.5
        #sm.delay = round(temp_diff / 5,2)
        #sm.crossfade = round(temp_diff / 10,2)
        #print(f"set delay to {sm.delay}")
        #print(f"set crossfade to {sm.crossfade}")
        #print('')