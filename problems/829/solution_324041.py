def soma_h(n):
    '''funcao que retorna a soma de frações com o denominador n crescente desde 1
    int -> float'''
    i=1
    while i<=n:
        h=h+(1/i)
        i=i+1
    return h