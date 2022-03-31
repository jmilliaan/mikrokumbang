import serial

s_port = ""
s_baud = ""
s_timeout = ""

class SerialKumbang:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port, self.baudrate, self.timeout)
        self.ser.reset_input_buffer()
    
    def serial_read(self):
        out = self.readline().decode('utf-8').rstrip()
        return out
    
    def serial_write(self, data):
        if type(data) != "string":
            data = string(data)
        self.ser.write(bytes(data))
        return 