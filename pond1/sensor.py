# Super Classe Sensor que define parametros de id e nome do sensor e um dict para valor e unidade de medida dos dados registrados 
class Sensor():
    def __init__(self, id=0, sensorName=None):
        self.id = id
        self.sensorName = sensorName
    
    def __str__(self):
        return f'\nSensor {self.id} - Sensor Name: {self.sensorName}'