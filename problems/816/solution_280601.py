def maiores(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort()
    sorted_list.index(n)
    alguns_numeros = sorted_list[ n for n in sorted_list if n > n ]
    return alguns_numeros