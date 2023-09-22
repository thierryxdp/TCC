def carros(pessoas, capacidade = 5):
    '''função que dado um número de pessoas retorna quantos carros são
    necessários para a viagem'''
    return round(pessoas/capacidade+0.5)