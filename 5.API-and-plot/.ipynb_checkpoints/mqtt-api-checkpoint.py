#!/usr/bin/env python
# coding: utf-8

# In[1]:


import eventlet
import json
from flask import Flask, jsonify, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap


# In[2]:


broker_url = 'eu.thethings.network'
port = 1883
app_id = 'fonexa'
app_key = 'ttn-account-v2.tni1mQx30F5yLzQaL4okkivKPSZT66v9XPKEjDrdG2o'
#app_id = 'simulacion-mqtt-api'
#app_key = 'ttn-account-v2.ruY7qlbxfqd9SVIOyDY2uRk4eou4sFcPpcx2A1__KXo'
topic = '+/devices/+/up'


# In[ ]:


app = Flask(__name__)
app.config['SECRET'] = ''
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = broker_url
app.config['MQTT_BROKER_PORT'] = port
app.config['MQTT_USERNAME'] = app_id
app.config['MQTT_PASSWORD'] = app_key
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

all_data = []

mqtt.subscribe(topic)


@app.route('/api/mqtt/1')

#For now, api v1 returns a huge json with all
#+/devices/+/up topic messages

def index():
    all_data_parsed =[{**d, 'payload':json.loads(d['payload'])} for d in all_data]
    print(all_data_parsed)
    return jsonify(all_data_parsed)
    #return render_template('index.html')

"""
@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()
"""

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    all_data.append(data)
    socketio.emit('mqtt_message', data=data)

"""
@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)
"""

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)


# In[ ]:




