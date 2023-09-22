def filtraMultiplos(lista_num, num):
    '''Função que dada uma lista com uma determinada quantidade de números e um número(num),
    retorna uma lista contendo todos os números da lista originais que são divisíveis pelo número(num).
    lista_num -> list
    num -> int'''
    
    i = 0
    lista_divisiveis = []
    
    while lista_num[i] % num == 0:
        lista_divisiveis += [lista_num[i]]
        
        i += 1
        
    return lista_divisiveis