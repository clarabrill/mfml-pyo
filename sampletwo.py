from time import sleep
import pyo
import json
import redis


with open('config.json', 'r') as fp:
    config = json.load(fp)

r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()

sf = pyo.SfPlayer("zoomsamples/lastdrop.wav", loop=True)  
ch = pyo.Chorus(sf).out()
hr = pyo.Harmonizer(sf).out()

server.start()


room_temp = None
temp = None

while True:
    temp = r.rpop('temp')
    if temp is None:
        #print("Queue is empty")
        sleep(1)

    else:
        print(f'got {temp} on a worker')
        if room_temp is None:
            room_temp = int(temp)

        temp_diff = abs(int(temp)  - room_temp) / 10000
        print(f'using temp_diff {temp_diff}')

   
        hr.transpo = temp_diff
        hr.feedback = .01 * temp_diff
        ch.bal = .6
        ch.depth = temp_diff * 6
        ch.feedback = temp_diff / 8