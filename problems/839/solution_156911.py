import math

def carros (pessoas , lugares = 5):
    '''calcula o numero de carros necessarios para levarem uma certa quantia de pessoas
       int, int, ---> int'''
    num_carros = math.ceil (pessoas / lugares)
    
    return num_carros