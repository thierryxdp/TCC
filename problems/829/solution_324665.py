def soma_h(n):
    '''Retorna o valor H com N termos onde N é um número inteiro dado como entrada
    int -> float'''
    lista = []
    for i in range(n):
        x = 1/i
        lista.append(x)
    return round(sum(lista),2)