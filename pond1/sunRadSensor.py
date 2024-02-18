import paho.mqtt.client as mqtt
from sensor import Sensor
import time
import random


# Criação da classe do Sensor de Radiação Solar, com os parametros de intensidade de radiação(0~1280W/m²) e comprimento de onda(300~1100nm)
class SunRadSensor(Sensor):
    def __init__(self, id, sensorName, radIntensity=0, waveLen=0):
        self.radIntensity = radIntensity
        self.waveLen = waveLen
        super().__init__(id, sensorName)
    
    def __str__(self):
        return f'\nSensor {self.id} - Sensor Name: {self.sensorName} \n Intensidade de Radiação: {self.radIntensity}W/m²\n Comprimento de Onda - {self.waveLen}nm \n'
    
    def generateData(self):
        self.radIntensity = round(random.triangular(955, 1280, 1080))
        self.waveLen = round(random.triangular(300, 1100, 600))

# Instanciando a classe
sunRadSen = SunRadSensor(1, 'RXW-LIB-900')


# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"python_publisher")
# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para publicar mensagens continuamente
try:
    while True:
        data = sunRadSen.generateData()
        message = str(sunRadSen)
        
        client.publish("sensor/sunRad", message)
        print(f"Publicado:\n {message}")
        time.sleep(4)
except KeyboardInterrupt:
    print("\n Publicação encerrada")

client.disconnect()