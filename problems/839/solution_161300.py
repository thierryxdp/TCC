def carros(p,c=5):
    """ calcula e retorna o número de veículos necessarios dados a quantidade de pessoas e a capacidade do veículo; caso c não seja fornecida a função considera seu valor como 5"""
    q=p//c
    return(ceil(q))