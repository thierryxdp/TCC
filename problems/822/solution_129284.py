def repetidos(listRep):
    '''função que recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao elemento antrior. list -> int'''
    cont = 0
    j = 1 
    while j < len(listRep):
        if listRep[j] == (listRep[j-1]):
            listRep.count(listRep[j])
            cont += 1
        j += 1
    return cont