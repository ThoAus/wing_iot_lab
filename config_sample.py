from types import SimpleNamespace

# Create a configuration object
CONFIG = SimpleNamespace()
CONFIG.MQTT_BROKER   = "0000000000000000000000000000.s1.eu.hivemq.cloud"
CONFIG.MQTT_PORT     = 8883
CONFIG.MQTT_TOPIC    = "kpi"
CONFIG.MQTT_USER     = "username"
CONFIG.MQTT_PASSWORD = "password"