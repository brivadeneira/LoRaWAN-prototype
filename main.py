# coding: utf-8

from flask import Flask, jsonify
from flask_mqtt import Mqtt

# config

broker_url = 'eu.thethings.network'
port = 1883
app_id = 'simulacion-lora'
app_key = 'ttn-account-v2.Ry5fpvakBfsaUGz7FRjFh1YFJl3s18D9W4jW7ynlWz8'
topic = '+/devices/+/up'


app = Flask(__name__)
app.config['SECRET'] = ''
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = broker_url
app.config['MQTT_BROKER_PORT'] = port
app.config['MQTT_USERNAME'] = app_id
app.config['MQTT_PASSWORD'] = app_key
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt()

mqtt.subscribe(topic)


all_data = []

@app.route('/')
def index():
    return jsonify(all_data)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    print('recibí un mensaje')
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    all_data.append(data)

if __name__ == "__main__":
    app.run()
