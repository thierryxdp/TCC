import math
def carros(pes,cap=5):
    '''calcula o número de carros necessários para viagem nessa rodovia , considerando que o número de pessoas é pes e a capacidade do veículo é cap , além de tais dados do enunciado'''
    carros=math.ceil(pes/cap)
    return carros