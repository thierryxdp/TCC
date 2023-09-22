def conta_numero(numero,matriz):
    """ procura um número em uma matriz e dis quantas vezes ele aparece;int,list->int"""
    i=0
    resposta=[]
    x=list.count(matriz[i],numero)
    while matriz[i] in matriz:
        if numero in matriz:    
            list.append(resposta,numero)
    return len(resposta)