import paho.mqtt.client as mqtt
import time

MQTT_CLIENT_ID = "publisher"

MQTT_HOST = 'localhost'
MQTT_PORT = 1883
QOS_LEVEL = 1

TOPIC_PREFIX = 'plc/product'

PRODUCT_NAME = "red-cable"
IS_GOOD_PRODUCT = True

POSITIVE_FOLDER_NAME = "pos"
NEGATIVE_FOLDER_NAME = "neg"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client connected")
    else:
        print("Bad connection result code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Client disconncted result code=", rc)


def on_publish(client, userdata, mid):
    print("Image published, mid=", mid)


def generate_topic_name(product_name, is_good_product):
    return f'{TOPIC_PREFIX}/{product_name}/{POSITIVE_FOLDER_NAME if is_good_product else NEGATIVE_FOLDER_NAME}'


client = mqtt.Client(client_id=MQTT_CLIENT_ID, clean_session=False)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect(MQTT_HOST, MQTT_PORT)
client.loop_start()

topic_name = generate_topic_name(product_name=PRODUCT_NAME, is_good_product=IS_GOOD_PRODUCT)

while True:
    f = open("sample.jpeg", "rb")
    img = f.read()
    byte_arr = bytearray(img)

    client.publish(topic_name, byte_arr, QOS_LEVEL)
    time.sleep(1)

client.loop_stop()
client.disconnect()