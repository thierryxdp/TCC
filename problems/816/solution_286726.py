def maiores( lista_int, N):
    '''funcao que recebe uma lista de inteiros e um n inteiro, e que retorna 
    outras lista com todos os números maiores que n de forma crescente
    list[int],int=>int'''
    lista_maiores= lista_int[:]
    for c in lista_int:
        if c >= N:
            lista_maiores.append(c)
            return lista_maiores 
        else:
            return []