# teste e garantia de recebimento de dados pelo Broker.
# Recebimento - garante que os dados enviados pelo simulador são recebidos pelo broker

import paho.mqtt.client as mqtt
from src.sensor import Sensor
import time
import random

class GenericSensor(Sensor):
    def __init__(self, id, sensorName, genericValue=0):
        self.genericValue = genericValue
        super().__init__(id, sensorName)
    
    def __str__(self):
        return f'\nSensor {self.id} - Sensor Name: {self.sensorName} \n Valor Genérico do Sensor: {self.genericValue}W/m²\n  \n'
    
    def generateData(self):
        self.genericValue = round(random.triangular(100, 500, 420))

def on_publish(client, userdata, mid):
    print("on_publish, mid {}".format(mid))

# Instanciando a classe
genSensor = GenericSensor(1, 'Generic Sensor-300X')

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"python_publisher")
client.on_publish = on_publish
# Conecte ao broker
client.connect("localhost", 1891, 60)



def getData():
    # contador para o numero de mensagens enviadas antes do  se encerrar
    count = 0
    # Loop para publicar mensagens continuamente
    try:
        while count < 3:
            data = genSensor.generateData()
            message = str(genSensor)
            tst = client.publish("sensor/sunRad", message, 2, True)
            tst.wait_for_publish()
            print(tst.is_published())
            print(f"Publicado:\n {message}")
            count += 1
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n Publicação encerrada")

    client.disconnect()

getData()