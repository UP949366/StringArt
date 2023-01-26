from flask import *
import json, time 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def first_entry(): 
    data_set = {'Page': 'Home', 'Message': 'First Entry', 'time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__': 
    app.run(port=7777)  