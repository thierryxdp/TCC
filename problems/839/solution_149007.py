import math

def carros(p,q=5):
    '''calcula a quantidade necessária de carros para um certo 
    grupo de p pessoas. Caso a capacidade do veículo não seja
    definida, será atribuido o valor convencional de 5 pessoas 
    por carro. p -> int | q -> int'''
    return math.ceil(p/q)