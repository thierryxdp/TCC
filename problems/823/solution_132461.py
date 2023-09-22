def faltante(lista):
    """desbobre o valor que está faltando em uma sequência;lista->int"""
    x=lista[-1]
    lista1=list(range(1,x+1))
    resposta=[]
    indice=0
    while(indice<len(lista)):
        if lista1[indice]!=lista[indice]:
            list.append(resposta,lista1[indice])
        indice+=1
    return resposta[0]