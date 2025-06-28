# WIFI CONFIGURATION
import machine, network
import config

# Connect to WIFI
def do_connect():

    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.ssid, config.password)
        while not wlan.isconnected():
            machine.idle()
    print('connection successful!')
    print('network config:', wlan.ipconfig('addr4'))
    return wlan

wlan = do_connect()

# MQTT CONFIGURATION
from upymqtt import MQTTClient
import ubinascii  

# Generate Unique Client ID
client_id = ubinascii.hexlify(machine.unique_id())

# Topics to subscribe and publish
topic_sub = b'settings'
topic_pub = b'kpi'

# MQTT Server Credentials
mqtt_server = config.mqtt_server
mqtt_user = config.mqtt_user
mqtt_pass = config.mqtt_pass
mqtt_port = config.mqtt_port

# Create a client instance; enable SSL for encrypted transport (TLS).
client = MQTTClient(
    client_id,
    mqtt_server,
    user=mqtt_user,
    password=mqtt_pass,
    port=mqtt_port,
    ssl=True,
    )

# Register the callback so incoming packets trigger `sub_cb`.
def sub_cb(topic, msg):
    global switch_value
    switch_value = int(msg)
    print(f"New Message: {topic}, {switch_value}")

client.set_callback(sub_cb)

# Open a network connection to the MQTT broker.
client.connect()
print(f"Connected to {mqtt_server} MQTT broker")


# Tell the broker which topic we want to listen to.
client.subscribe(topic_sub)
print(f"Subscribed to {topic_sub} topic")