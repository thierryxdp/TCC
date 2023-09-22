def faltante(list):
    list_s = sort(list)
    list_c = range(list_s[0], list_s[len(list) - 1])
    missing = 0
    i = 0
    while i < len(list):
        if list_c[i] not in list_s:
            missing = list_c[i]
        i += 1
    return missing