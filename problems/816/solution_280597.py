def maiores(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort()
    alguns_numeros = sorted_list[2:7:2]
    return sorted_list