# 🕹️ DIY Custom Joystick & Mouse with STM32F411CE (BlackPill)

This project transforms an STM32F411CE (BlackPill) and a standard analog joystick module into a highly customizable, cross-functional input device. By bypassing the native USB HID endpoint limitations of the STM32, this project uses a highly stable **Serial-to-OS architecture**, allowing you to use the hardware as a PC Mouse, an Xbox 360 Gamepad, or whatever you want to program it to be!

## ✨ The Power of Customization
This isn't just a basic joystick. Because the heavy lifting (interpreting inputs and triggering OS events) is done by Python scripts on your computer, the possibilities are endless:
* **Endlessly Expandable:** Want to add more buttons, sliders, or sensors? Just wire them to the BlackPill and add a single variable to the `print()` statement in the STM32 firmware.
* **Ergonomic Adaptability:** The current mouse script features a software-based **90-degree axis rotation**. It maps physical inputs perfectly to how the module fits comfortably in your hand, without needing to desolder or rebuild the hardware.
* **Multi-Role Device:** Switch from a gaming device (Xbox 360 emulator) to a productivity tool (Mouse) simply by stopping one Python script on your PC and running another. No need to reflash the microcontroller!

## 🛠️ Hardware Requirements
* 1x **STM32F411CE (WeAct BlackPill)**
* 1x **Analog Joystick Module** (e.g., KY-023)
* **9x Jumper Cables** (Female-to-Female or Male-to-Female depending on your pins)
* 1x **USB to USB-C Cable** (for power and data transfer)

## 📸 Project Components
<div align="center">
  <img width="200" alt="Joystick Setup View 1" src="https://github.com/user-attachments/assets/8632cd4d-f6ca-4f30-bf63-cf3f0dc92934" /><img width="300" alt="Joystick Setup View 2" src="https://github.com/user-attachments/assets/aa8d747c-a112-440e-b130-08176ad3c4f6" /><img width="204.8" alt="Joystick Setup View 3" src="https://github.com/user-attachments/assets/a7d66192-bda5-4954-b32a-a324a4dd8e07" />
</div>

## 🧠 Architecture Overview
The project is divided into two components working as a team:

1. **The Hardware (`stm32_circuitpython/`)**:
    * Runs **CircuitPython**.
    * `code.py` constantly reads the analog values (X, Y) and digital state (Button) from the joystick's potentiometers.
    * Streams raw data seamlessly over the USB Serial port (e.g., `12000,-4500,1`).
    * *Note: The `boot.py` file must remain completely blank to free up USB endpoints and prevent the BlackPill from entering Safe Mode.*

2. **The Software (`scripts_windows/`)**:
    * A Python listener running on your Windows PC that grabs data from the COM Port.
    * **`mouse_joystick.py`**: Uses the `pynput` library to translate Serial data into cursor movements and left-clicks.
    * **`xbox_joystick.py`**: Uses the `vgamepad` library to emulate a physical Xbox 360 controller on a driver level, guaranteeing 100% native game compatibility.

## 🔗 Useful Links & Tools
* **Hardware Reference:** [WeAct Black Pill V3.0 (STM32-base)](https://stm32-base.org/boards/STM32F401CEU6-WeAct-Black-Pill-V3.0.html)
* **Firmware:** [CircuitPython for STM32F411CE](https://circuitpython.org/board/stm32f411ce_blackpill/)
* **Libraries:** [CircuitPython Libraries Bundle](https://circuitpython.org/libraries)
* **Flasher Tool:** [STM32CubeProgrammer](https://www.st.com/content/st_com/en/stm32cubeprogrammer.html)
* **IDE:** [Thonny](https://thonny.org/)
