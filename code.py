import time
import board
import analogio
import digitalio

eixo_x = analogio.AnalogIn(board.A0)
eixo_y = analogio.AnalogIn(board.A1)

botao = digitalio.DigitalInOut(board.A2)
botao.direction = digitalio.Direction.INPUT
botao.pull = digitalio.Pull.UP

def mapear_para_xbox(valor_cru):
    # 0~65535 to Xbox (-32768 a 32767)
    
    if 30768 < valor_cru < 34768:
        return 0
    
    valor = int(valor_cru - 32768)
    
    if valor > 32767: return 32767
    if valor < -32768: return -32768
    return valor

while True:
    x = mapear_para_xbox(eixo_x.value)
    
    y = mapear_para_xbox(eixo_y.value) * -1 
    
    b = 1 if not botao.value else 0
    
    print(f"{x},{y},{b}")
    
    time.sleep(0.01) 
