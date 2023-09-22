def repetidos(lista):
    '''função que recebe uma lista de números e retorna os consecutivos repetidos; list => int'''
    repet = 0
    i = 0
    for i in range (len(lista)-1):
        if lista[i]==(lista[i+1]):
            repet=repet+1
        i=i+1
    return repet