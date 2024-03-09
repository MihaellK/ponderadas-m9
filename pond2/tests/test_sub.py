import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print(f"Connected with result code {rc}")
  client.subscribe("test/topic", 2)

def on_message(client, userdata, msg):
  print(f"Received message: {msg.topic} {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "python_subscriber") #(mqtt.CallbackAPIVersion.VERSION1, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1891, 60)

client.loop_forever()