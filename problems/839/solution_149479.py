import math 
def carros (x,y=5):
    '''calcula o numero de carros necessarios para o transporte de pessoas,
    dados x(número de pessoas) e y(capacidade do veiculo) '''
    return round(x/y)