def conta_numero(num,ls):
    vzs = 0
    for listas in ls:
        for numero in listas:
            if numero == num:
                vzs += 1
    return vzs