def carros(pessoas, capacidade=5):
    '''recebe o numero de pessoas e a capacidade do veiculo (com 5 como padrao) e retorna o numero de carros que serao necessarios''' 
    x = pessoas/capacidade
    y = pessoas//capacidade
    if (x < y + 0.51):
        total = round(x) + 1
    else:
        total = x
    return total