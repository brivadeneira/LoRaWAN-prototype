#!/usr/bin/env python
# coding: utf-8

# In[16]:


import base64
import datetime

import dash  
import dash_core_components as dcc
import dash_html_components as html
import requests

import random

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
    
    for entry in data:
        devs.append(entry['payload']['dev_id'])
    unique_devs = set(devs)

    for dev in unique_devs:
        options.append({'label': dev, 'value': dev})
    if options:
        options.append({'label': 'todos', 'value': 'todos'})
    return options


def parse_date_time(date_time):
    """
    Returns a datetime object,
    expects a string like '2019-11-26T21:15:10.161219748Z'
    but uses just 10.161219 information of seconds
    """
    #print(date_time)
    #return datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    return datetime.datetime.strptime(date_time[:-4], 
                                      '%Y-%m-%dT%H:%M:%S.%f').astimezone()

def get_data_from_bytes(data_bytes):
    """
    Return a tuple with data
    Expects a payload like:
    'Temperature : %.2f, Humidity : %.2f\r\n'
    """
    data_str = str(data_bytes).split("'")[1]
    print(data_str)
    #temp_str = str(data_bytes)
    #temp = temp_str.split("'")[1].split('= ')[1] # this parser matches with mbed sim
    if '\'' in data_str or 'x' in data_str:
        temp = 26.7
        hum = 55
    else:
        temp_hum_list =  data_str.split(',')
        temp = float(temp_hum_list[0].split(' : ')[1])
        hum = float(temp_hum_list[1].split(' : ')[1])
    return (temp, hum)

def gen_dict_plot(data):
    """
    Return a dict with form:
    {'dev_id': 
        {'times': ['aaaa-mm-ddThh:mm:ss', 'aaaa-mm-ddThh:mm:ss'], 
                'temps': [xx.y, xx.y],
                'hums': [xx.y, xx.y]}
        }
    Expects data from API
    """
    ready_to_plot_data = {'todos': {'times' : [], 'temps' : [], 'hums': []}}
    # Create empty dicts for each dev
    for dev in unique_devs:
        ready_to_plot_data[dev] = {'times' : [], 'temps' : [], 'hums': []}
    # Load that empty dict with data    
    for entry in data:
        dev_id = entry['payload']['dev_id']
        #date_time_str = entry['payload']['metadata']['gateways'][0]['time']
        date_time_str = entry['payload']['metadata']['time']
        time = parse_date_time(date_time_str) #time ready to load
        
        if dev_id == 'arduino-uno-nodo':
            import random
            temp = random.randint(25, 28)
            hum = random.randint(60, 70)
            ready_to_plot_data[dev_id]['times'].append(time)
            ready_to_plot_data[dev_id]['temps'].append(temp)
            ready_to_plot_data[dev_id]['hums'].append(hum)

            ready_to_plot_data['todos']['times'].append(time)
            ready_to_plot_data['todos']['temps'].append(temp)
            ready_to_plot_data['todos']['hums'].append(hum)

        payload_raw = entry['payload']['payload_raw']
        print(payload_raw)
        data_payload = decode_payload(payload_raw) #decoded payload raw
        print(data_payload)
        temp, hum = get_data_from_bytes(data_payload) #temp, hum ready to load
                
        ready_to_plot_data[dev_id]['times'].append(time)
        ready_to_plot_data[dev_id]['temps'].append(temp)
        ready_to_plot_data[dev_id]['hums'].append(hum)
                
        ready_to_plot_data['todos']['times'].append(time)
        ready_to_plot_data['todos']['temps'].append(temp)
        ready_to_plot_data['todos']['hums'].append(hum)
    return ready_to_plot_data

def get_plot_colors():
    """
    Return a list of tuples of 3 color combinations,
    if you must to plot more than 2 groups of data,
    you have to generate more pairs of colors
    """
    colors = [('#0040db', '#00aedb'),
             ('#f37735', '#f3d635'),
             ('#00b159', '#00b101')]
    return colors

#external_stylesheets = ['https://codepen.io/lynnandtonic/pen/NWWmzjr.css']
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
            #interval=5 * 60 * 1000,
            n_intervals=0
        )
    #html.Div(id='output-container')
])

@dash_app.callback(
    dash.dependencies.Output('lora-graph', 'figure'),
    [dash.dependencies.Input('dev-dropdown', 'value'), 
     dash.dependencies.Input('interval-component', 'n_intervals')])

def update_graph(selected_dev, n):
    url_data = 'http://0.0.0.0:5000/api/mqtt/1'
    data = requests.get(url_data).json()
    options = get_options(data)
    ready_to_plot_data = gen_dict_plot(data)

    if not selected_dev:
        return {'data': []}
    
    elif selected_dev == 'todos':
        colors = get_plot_colors()
        plot_dict = {'data': []}
        for i, dev in enumerate(unique_devs):
            dev_dict_temp = {
                'x': ready_to_plot_data[dev]['times'],
                'y': ready_to_plot_data[dev]['temps'],
                'name': 'Temp, ' + dev,
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': colors[i][0],
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
            }
            dev_dict_hum = {
                'x': ready_to_plot_data[dev]['times'],
                'y': ready_to_plot_data[dev]['hums'],
                'name': 'Hum, ' + dev,
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': colors[i][1],
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
                }
            plot_dict['data'].append(dev_dict_temp)
            plot_dict['data'].append(dev_dict_hum)
        todos_dict_temp = {
                'x': ready_to_plot_data['todos']['times'],
                'y': ready_to_plot_data['todos']['temps'],
                'name': 'Temp, todos',
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': colors[-1][0],
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
                }
        todos_dict_hum = {
                'x': ready_to_plot_data['todos']['times'],
                'y': ready_to_plot_data['todos']['hums'],
                'name': 'Hum, todos',
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': colors[-1][1],
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
                }
        plot_dict['data'].append(todos_dict_temp)
        plot_dict['data'].append(todos_dict_hum)
        return plot_dict
                
    else:
        return {
            'data': [
                {
                'x': ready_to_plot_data[selected_dev]['times'],
                'y': ready_to_plot_data[selected_dev]['temps'],
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
                },
                {
                'x': ready_to_plot_data[selected_dev]['times'],
                'y': ready_to_plot_data[selected_dev]['hums'],
                'name': 'Humedad',
                'mode': 'lines',
                'marker': {'size': 1},
                'showlegend': True,
                'line': {'shape': 'linear',
                         'color': '#cd6838',
                         'width': 2,
                         'dash': 'solid',
                         'sumplify': True,
                         'type': 'scatter'}
                },
            ]
        }

if __name__ == '__main__':
    dash_app.run_server(
        host="localhost",
        port=8001,
        debug=True)

