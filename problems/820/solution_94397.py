def posLetra(frase,letra,numero):
    """esta funçao retorna a posição da letra na frase dada de acordo com a ocorrência pré definida pelo numero
    str, str, int-> int"""
    indice=0
    lista=[]
    while indice<len(frase):
        lista+=[frase[indice]]
        indice+=1
    lista1=[]
    indice1=0
    while indice1<len(lista):
        if lista[indice1]==letra:
            lista1+=[frase[indice1]]
        indice1+=1
    if numero>len(lista1):
        return -1
    b=indice1-1
    a=lista1[b]
    return a