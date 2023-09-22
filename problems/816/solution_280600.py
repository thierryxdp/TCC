def maiores(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort()
    sorted_list.index(n)
    alguns_numeros = sorted_list[ elem for elem in full_list if elem > num ]
    return alguns_numeros