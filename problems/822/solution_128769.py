def repetidos (l):
    """que receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista ́e igual ao elemento anterior"""
    i=1
    resposta=0
    while l[i]==l[i-1]:
        resposta=resposta+1
    i=i+1
    return resposta