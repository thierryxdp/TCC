def repetidos(num):
    """funcao que, dada uma lista de numeros como entrada, retorna quantas vezes um elemento da lista e igual ao seu elemento anterior
    list(float)--->int"""
    i=0
    repetidos=0
    while i<len(num):
        if num[i]==num[i+1]:
            repetidos=repetidos+1
        i=i+1
    return repetidos