def maiores( lista_int, N):
    '''funcao que recebe uma lista de inteiros e um n inteiro, e que retorna 
    outras lista com todos os números maiores que n de forma crescente
    list[int],int=>int'''
    for N in lista_int:
        if c >= N:
            list.append(lista_int, c)
            list.reverse(lista_int)
            i=list.index(lista_int,c)
            lista_maiores=lista_int[0:i]
            list.sort(lista_int)
            return lista_maiores 
        else:
            return []