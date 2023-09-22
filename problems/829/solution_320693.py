def soma_h(N):
    '''função que recebe um número inteiro N e retorna H, que é a soma 1+(1/2)+(1/3)+...+(1/N).
    int -> float'''
    contador = 1
    H = []
    for elemento in range(N):
        list.append(H,1/contador)
        contador = contador + 1
    return round(sum(H),2)