def soma_h(n):
    '''Retorna a soma de 1 + 1/2 + 1/3... até 1/n.
       int -> float'''
    i = 0
    h = float()
    soma = 0
    resultados=[]
    while i < n:
        h = 1/(1 + i)
        list.append(resultados, h)
        i = i + 1    
    for n in resultados:
        soma += n
    return round(soma, 2) and resultados