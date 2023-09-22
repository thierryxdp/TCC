def conta_numero(numero,matriz):
    """ procura um número em uma matriz e dis quantas vezes ele aparece;int,list->int"""
    i=0
    resposta=[]
    while matriz[i] in matriz:
        if numero in matriz[i]:
        x=list.count(matriz[i],numero)
        list.append(resposta,x)
    return len(resposta)