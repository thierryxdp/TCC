def maiores(lista_num,n):
    ''' retorna uma lista em que os números maiores que n 
    (número a ser incluso) estão em ordem crescente,
    [int],int->[int]'''
   
    if lista_num[:]<n:
        return list.sort(lista_num)
    else:
        return []