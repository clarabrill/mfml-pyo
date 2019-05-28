from flask import Flask, request
import redis

# imported flask module - flask is a class, request is an object (an instantiated class)
# imported redis library which is module
# modules - look at learn python the hard way - collections of code that are importable
# flask is the web server library
# mac runs flask to listen for http requests coming from pi & respond with 'OK' (200)
# request object accesses request data while responding to http request

# creates object from class : the flask web server app itself 
# classes start with capital letters, storing in variable called app
app = Flask(__name__)

# importing from redis module redis class, instantiating that and saving it to r
# redis is a data store (stores data), and we have some data..
# great at performing queue, list - first in, first out 
# FIFO - first in first out - first thing that pops is the first thing that went in 
# think of line of ppl 
# redis communicates with the flask web server & pyo audio server
r = redis.Redis(host='localhost', port=6379, db=0)

# listen for http POST requests at path /temp (only listening to /temp)
# r.lpush - at key temp, create a list (if doesnt exist already) & PUSH data from the left side (emulate queue)
@app.route('/temp', methods=['POST'])
def temp():
    data = request.get_data(as_text=True)
    print(f"Got data : {data}")
    r.lpush('temp', data)
    return 'OK'

# method is POST
# return 'OK' is response to the http requester