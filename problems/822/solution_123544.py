def repetidos(lista):
    """ recebe uma lista e torna a qunatidade de vezes que um lemento da lista 
    é igual ao anterio;list->int"""
    indice=0
    resposta=[]
    lista2=lista[:indice]
    while(indice<len(lista)):
        if (lista[indice] in lista2):
            (list.append(resposta,list.count(lista2,indice)))
    indice+=1
    return resposta