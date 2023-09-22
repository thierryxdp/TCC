def soma_h(n):
    '''Retorna o valor H com N termos onde N é um número inteiro dado como entrada
    int -> float'''
    lista = []
    for i in range(1,n,-1):
        x = 1/i
        lista.append(x)
    return round(sum(lista),2)