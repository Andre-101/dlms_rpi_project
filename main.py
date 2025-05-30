from dlms_client import DLMSMeterClient

if __name__ == "__main__":
    meter = DLMSMeterClient(port="/dev/ttyUSB0", baudrate=9600)
    meter.connect()

    print("Leyendo datos instantáneos...")
    result = meter.read_instantaneous()
    print(result)

    meter.disconnect()
