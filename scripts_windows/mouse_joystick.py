import serial
from pynput.mouse import Controller, Button
import sys

PORT_COM = "COM3"  
BAUD_RATE = 115200

mouse = Controller()

# Adjust the sensitivity of your new mouse here!
MAX_SPEED = 15 

try:
    ser = serial.Serial(PORT_COM, BAUD_RATE, timeout=0.1)
    ser.dtr = True 
    ser.rts = True
    print("Joystick operating as Mouse! Press Ctrl+C to exit.")
except serial.SerialException:
    print("Error: COM port not found or is in use.")
    sys.exit()

estado_botao_anterior = 0

while True:
    try:
        linha = ser.readline().decode('utf-8').strip()
        if linha:
            x, y, botao = map(int, linha.split(','))

            # Convert the scale from -32768 to 32767 to pixel speed on screen.
            move_x = int((y / 32768.0) * MAX_SPEED) * -1

            # The screen Y axis grows downward.
            # Invert the sign so that "up" moves the cursor up.
            move_y = int((x / 32768.0) * MAX_SPEED) * -1 

            # Move the cursor on screen by adding the offset to the current position
            if move_x != 0 or move_y != 0:
                mouse.move(move_x, move_y)

            # Left click control
            if botao == 1 and estado_botao_anterior == 0:
                mouse.press(Button.left)  # Hold the click (allows dragging folders)
            elif botao == 0 and estado_botao_anterior == 1:
                mouse.release(Button.left) # Release the click
            
            estado_botao_anterior = botao
            
    except ValueError:
        pass
    except KeyboardInterrupt:
        print("\nShutting down mouse control...")
        break

ser.close()