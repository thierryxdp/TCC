def faltante(list):
    list = sorted(list)
    for r in list:
        if 1 not in list:
            return 1
        if (r+1) not in list:
            return r+1