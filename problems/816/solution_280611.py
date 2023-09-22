def maiores(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort()
    alguns_numeros = list.index(sorted_list,n)
    
    return alguns_numeros