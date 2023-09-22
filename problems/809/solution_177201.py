def intercala(lista1, lista2):
    '''funcao que intercala listas
    entrada: lista
    saida: lista 
    '''
    return lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]