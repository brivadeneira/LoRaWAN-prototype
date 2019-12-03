# MQTT API and Dash plot

Executing two simple python scripts, you can set up a MQTT API to get LoRaWAN nodes data in a json format and next create a real time plot with dash.



## Instructions

```
pip install -r requirements.txt
```

* Go to thethingsnetworks.
* Go to `console` clicking in your avatar.

![](https://i.imgur.com/ptdWS4E.png)

* Go to `application`.
* Select the app in which you registered the nodes.
* Go to `overview`, get the `access key`

* Go to `mqtt-api.py` file and change `app_id` and `app_key` parameters according to yout app:

```
app_id = 'fonexa'
app_key = 'ttn-account-v2.tni1mQx30F5yLzQaL4okkivKPSZT66v9XPKEjDrdG2o'
```

> lines 20, 21

`pyton mqtt-api.py`
* Go to [0.0.0.0/api/mqtt/1](0.0.0.0/api/mqtt/1)

`pyton dash_app.py`
* Go to [localhost:8001](localhost:8001)