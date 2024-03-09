import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
  print(f"Message published mid: {mid}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "python_subscriber")
client.on_publish = on_publish
client.connect("localhost", 1891, 60)

topic = "test/topic"
payload = "Hello MQTT with QoS 2"
qos = 2

client.publish(topic, payload, qos)
client.loop_forever()