def faltante(lista):
    """desbobre o valor que está faltando em uma sequência;lista->int"""
    x=lista[-1]
    lista1=list(range(1,x+1))
    lista2=list.append(lista1,(x+1))
    lista3=list.append(lista,0)
    indice=0
    resposta=[]
    while(indice<len(lista)):
        if lista[indice]!=lista1[indice]:
            list.append(resposta,lista1[indice])
        indice+=1
    return resposta[0]