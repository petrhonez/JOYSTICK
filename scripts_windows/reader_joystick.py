import serial
import vgamepad as vg
import time
import sys

# ---> CONFIRM IF THIS IS STILL COM3 <---
PORT_COM = "COM3"  
BAUD_RATE = 115200

    # Create the virtual Xbox 360 controller
gamepad = vg.VX360Gamepad()
print("Virtual Xbox 360 controller connected!")

try:
    # Start serial communication
    ser = serial.Serial(PORT_COM, BAUD_RATE, timeout=0.1)
    
    # THE TRICK IS HERE: Notify the BlackPill that the PC is listening
    ser.dtr = True
    ser.rts = True
    
    print(f"Reading data from {PORT_COM}. Press Ctrl+C to exit.")
except serial.SerialException:
    print(f"Error: Could not connect to {PORT_COM}.")
    print("Is Thonny open? CLOSE Thonny's serial connection first!")
    sys.exit()

while True:
    try:
        linha = ser.readline().decode('utf-8').strip()
        if linha:
            # Print incoming data to the console so we can verify
            print(f"Received data: {linha}")
            
            # Split the values sent from the STM32
            x, y, botao = map(int, linha.split(','))

            # Update the virtual axes
            gamepad.left_joystick(x_value=x, y_value=y)

            # Update the A button
            if botao == 1:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

            # Send the update to the system
            gamepad.update()
            
    except ValueError:
        pass
    except KeyboardInterrupt:
        print("\nClosing controller...")
        break

ser.close()