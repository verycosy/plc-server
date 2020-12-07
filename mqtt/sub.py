import paho.mqtt.client as mqtt
import datetime
import os
import pathlib

MQTT_CLIENT_ID = "subscriber"

MQTT_HOST = 'localhost'
MQTT_PORT = 1883
QOS_LEVEL = 1

TOPIC_PREFIX = 'plc/product'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client connected")
    else:
        print("Bad connection result code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Client disconncted result code=", rc)


def on_subscribe(client, userdata, mid, granted_qos):
    print(f'subscribed, mid={mid}, qos={granted_qos}')


def on_message(client, userdata, msg):
    product_info = msg.topic.split('/')

    product_name = product_info[2]
    neg_or_pos = product_info[3]
    
    current_date = datetime.datetime.now()

    folder_path = os.path.join("..", "static", "data", product_name, "test", neg_or_pos)
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)

    print(f'Save image to {folder_path}')
    f = open(f'{folder_path}/{current_date}.jpeg', 'wb')
    f.write(msg.payload)
    f.close()


client = mqtt.Client(client_id=MQTT_CLIENT_ID, clean_session=False)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT)

client.subscribe(f'{TOPIC_PREFIX}/#', QOS_LEVEL)
client.loop_forever()