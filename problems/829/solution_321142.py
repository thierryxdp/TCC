def soma_h(N):
    """ calcula a soma de uma fórmula de N termos de 1 até 1/N; int->float"""
    lista=list(range(2,N+1))
    resposta=[1]
    for numero in lista:
        list.append(resposta,1//numero)
    return round(sum(resposta),2)