def maiores(lista, n):
    '''uma função que retorna uma lista contendo todos números inteiros maiores que n
    lista, int -> lista'''
    nlista = []
    for numero in lista:
        if numero > n:
            list.append(nlista, numero)
    list.sort(nlista)
    return nlista

def acima_da_media(notas):
    '''uma função que retorna uma lista com as notas que ficaram acima da média
    lista -> lista'''
    return maiores(notas,len(notas)//~2)