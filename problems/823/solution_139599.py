def faltante(list):
    list = sprted(list)
    for r in list:
        if (r + 1) not in list:
            return r +1