def faltante(list):
    list.sort()
    i = 1
    while i <= (len(list)):
        if i != list[i-1]:
            return i
        i += 1

    return len(list) + 1