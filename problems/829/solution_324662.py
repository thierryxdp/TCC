def soma_h(n):
    '''Retorna o valor H com N termos onde N é um número inteiro dado como entrada
    int -> float'''
    lista = []
    for i in range(n+1):
        x = pow(-1,i)/2*i+1
        lista.append(x)
    return sum(lista)