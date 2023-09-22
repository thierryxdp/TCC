def maiores( lista_int, N):
    '''funcao que recebe uma lista de inteiros e um n inteiro, e que retorna 
    outras lista com todos os números maiores que n de forma crescente
    list[int],int=>int'''
    for c in lista_int:
        if c >= N:
            i=list.index(lista_int,c)
            lista_maiores=lista_int[0:i]
            lista_maiores.append(c)
            lista_maiores.reverse(lista_maiores)
            lista_maiores.sort(lista_maiores)
            return lista_maiores 
        else:
            return []