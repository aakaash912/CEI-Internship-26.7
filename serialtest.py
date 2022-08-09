import serial
value=serial.Serial('COM5',9600)
val=1
value.write(val)
print(value)