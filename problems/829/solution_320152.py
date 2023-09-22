def soma_h(n):
    '''Retorna a soma de 1 + 1/2 + 1/3... até 1/n.
       int -> float'''
    h = float()
    soma = 0
    resultados=[]
    for i in range(n):
        h = 1/(1 + i)
        list.append(resultados, h)   
    for n in resultados:
        soma += n
    return round(soma, 2)