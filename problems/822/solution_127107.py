def repetidos(lista):
    '''Função que recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list[int]->int'''
    indece=1
    S=[]
    while indece<=len(lista):
        if lista[indece-1:indece]==lista[indece:indece+1]:
            list.append(S,lista[indece:indece+1])
        indece=indece+1
    return len(S)