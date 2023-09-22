def repetidos(lista):
    """ retorna o número de vezes que um elemento da lista é igual ao anterior;list->int"""
    resposta=[]
    indice=0
    x= indice-1
    while(indice<len(lista)):
        if lista[indice]==lista[x]:
            list.append(resposta,lista[indice])
        indice+=1
    return (resposta)