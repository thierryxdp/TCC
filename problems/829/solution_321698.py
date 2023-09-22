def soma_h(n):
    '''dado um número inteiro(n), retorna H;
    Ex: H = 1 + 1/2 + 1/3 + ... + 1/n
    int -> float'''
    lista = []
    for i in range(1,n+1):
        lista.append(1/i)
    s = sum(lista)
    return round(s,2)