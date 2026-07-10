import time
import board
import analogio
import digitalio

# Configuração dos Pinos
eixo_x = analogio.AnalogIn(board.A0)
eixo_y = analogio.AnalogIn(board.A1)

botao = digitalio.DigitalInOut(board.A2)
botao.direction = digitalio.Direction.INPUT
botao.pull = digitalio.Pull.UP

def mapear_para_xbox(valor_cru):
    # Transforma a leitura de 0~65535 para a escala do Xbox (-32768 a 32767)
    # Define uma zona morta no centro para o controle não "puxar" sozinho
    if 30768 < valor_cru < 34768:
        return 0
    
    valor = int(valor_cru - 32768)
    
    # Trava os limites para não bugar o controle
    if valor > 32767: return 32767
    if valor < -32768: return -32768
    return valor

while True:
    x = mapear_para_xbox(eixo_x.value)
    
    # O eixo Y físico geralmente é invertido, então multiplicamos por -1
    y = mapear_para_xbox(eixo_y.value) * -1 
    
    # O botão dá 0 quando apertado (por causa do GND)
    b = 1 if not botao.value else 0
    
    # Imprime no padrão "X,Y,BOTAO"
    print(f"{x},{y},{b}")
    
    time.sleep(0.01) # Atualiza a 100 frames por segundo