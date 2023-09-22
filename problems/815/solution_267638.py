def insert_sort(sorted_list, n):
    """ Função que dada uma lista ordenada de números inteiros e um número inteiro n, 
    inclua n na posição correta, ou seja, que a lista continue ordenada"""
    sorted_list.append(n)
    sorted_list.sort()

#    return list.sort(sorted_list)
    return sorted_lis