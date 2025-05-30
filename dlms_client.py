import serial
from gurux_dlms.GXDLMSClient import GXDLMSClient
from gurux_common.enums import InterfaceType
from gurux_dlms.enums.Security import Security

class DLMSMeterClient:
    def __init__(self, port, baudrate):
        self.port = serial.Serial(port, baudrate=baudrate, bytesize=8, parity='N', stopbits=1, timeout=1)
        self.client = GXDLMSClient(
            interfaceType=InterfaceType.WRAPPER,
            useLogicalNameReferencing=True,
            clientAddress=16,
            serverAddress=1,
            authentication=0,
            password="12345678",
            security=Security.NONE
        )

    def connect(self):
        print("Conectando al medidor (simulado)...")
        # Aquí se implementaría el handshake real DLMS: SNRM, AARQ, etc.

    def read_instantaneous(self):
        # Ejemplo simulado de lectura
        return {
            "voltage_A": "230.1 V",
            "current_A": "5.2 A",
            "power_factor": "0.97",
            "frequency": "60 Hz"
        }

    def disconnect(self):
        self.port.close()
