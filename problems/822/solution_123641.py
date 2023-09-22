def repetidos(lista):
    """ retorna o número de vezes que um elemento da lista é igual ao anterior;list->int"""
    resposta=[]
    indice=0
    lista2=lista[indice:indice-1]
    while(indice<len(lista)):
        if lista[indice] in lista2:
            list.append(resposta,lista[indice])
        indice+=1
    return (resposta)