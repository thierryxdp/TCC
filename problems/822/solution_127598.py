def repetidos (lista):
    '''função que recebe uma lista de numeros e retorna o nu
    mero de vezes que um elemento da lista é igual ao anteri
    or; list->int'''
    lista_resp=[]
    indice=0
    while indice<len(lista):
        if lista[indice]==((lista[indice])+1):
            lista_resp=lista_resp+lista[indice]
        elif lista[indice]!=((lista[indice])+1):
            lista_resp
        indice+=1
    return lista_resp