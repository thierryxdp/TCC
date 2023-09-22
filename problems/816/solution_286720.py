def maiores( lista_int, N):
    '''funcao que recebe uma lista de inteiros e um n inteiro, e que retorna 
    outras lista com todos os números maiores que n de forma crescente
    list[int],int=>int'''
    lista_maiores= list()
    lista_int.sort()
    for c in lista_int:
        if c >= N:
            lista_maiores.append(c, lista_int)
            return lista_maiores 
        else:
            return []