def conta_numero(num,ls):
    vzs = 0
    for listas in ls:
        for número in listas:
            if número == num:
                vzs += 1
    return vzs