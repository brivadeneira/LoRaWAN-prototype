#!/usr/bin/env python
# coding: utf-8

# In[16]:


import base64
import datetime

import dash  
import dash_core_components as dcc
import dash_html_components as html
import requests


def decode_payload(payload_raw):
    return base64.b64decode(payload_raw)

def get_options(data):
    """
    Generate a list with form:
    [{'label': dev_id, 'value': dev_id}]
    """
    global unique_devs
    devs = []
    options = []
    #devs_list = [{'label': 'todos', 'value': 'todos'}]
    
    for entry in data:
        devs.append(entry['payload']['dev_id'])
    unique_devs = set(devs)

    for dev in unique_devs:
        options.append({'label': dev, 'value': dev})
    if options:
        options.append({'label': 'todos', 'value': 'todos'})
    return options


def parse_date_time(date_time):
    return datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%fZ')

def get_temp_from_bytes(temp_bytes):
    temp_str = str(temp_bytes)
    temp = temp_str.split("'")[1].split('= ')[1]
    return float(temp)

def gen_dict_plot(data):
    """
    Generate a dict with form:
    {'dev_id': 
        {'times': ['aaaa-mm-ddThh:mm:ss', 'aaaa-mm-ddThh:mm:ss'], 
                'temps': [xx.y, xx.y]}
        }
    """
    time_temp_data = {'todos': {'times' : [], 'temps' : []}}
    for dev in unique_devs:
        print('dev in data', dev)
        time_temp_data[dev] = {'times' : [], 'temps' : []}
    for entry in data:
        #if entry['payload']['dev_id'] == dev:
        dev_id = entry['payload']['dev_id']
        time_str = entry['payload']['metadata']['gateways'][0]['time']
        time = parse_date_time(time_str) #time ready to load

        payload_raw = entry['payload']['payload_raw']
        temp_payload = decode_payload(payload_raw)
        temp = get_temp_from_bytes(temp_payload) #temp ready to load
                
        time_temp_data[dev_id]['times'].append(time)
        time_temp_data[dev_id]['temps'].append(temp)
                
        time_temp_data['todos']['times'].append(time)
        time_temp_data['todos']['temps'].append(temp)
    return time_temp_data

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dash_app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)

url_data = 'http://0.0.0.0:5000/api/mqtt/1'
data = requests.get(url_data).json()
options = get_options(data)
data_dict = gen_dict_plot(data)


dash_app.layout = html.Div([
    dcc.Dropdown(
        id='dev-dropdown',
        options=options,
        placeholder='Filtro por dispositivo: '
    ),
    dcc.Graph(id='lora-graph'),
            dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    #html.Div(id='output-container')
])

@dash_app.callback(
    dash.dependencies.Output('lora-graph', 'figure'),
    [dash.dependencies.Input('dev-dropdown', 'value')])

def update_graph(selected_dev):
    url_data = 'http://0.0.0.0:5000/api/mqtt/1'
    data = requests.get(url_data).json()
    options = get_options(data)
    data_dict = gen_dict_plot(data)
    print(data_dict, selected_dev, type(selected_dev))

    if not selected_dev:
        return {'data': []} 
    else:
        return {
            'data': [
                {
                'x': data_dict[selected_dev]['times'],
                'y': data_dict[selected_dev]['temps'],
                'name': 'Temperatura',
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': '#1f77b4',
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
                }]
        }

if __name__ == '__main__':
    dash_app.run_server(
        host="localhost",
        port=8001,
        debug=True)

