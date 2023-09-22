def faltante(l):
    i = 0
    value = 0
    ls = sorted(l)
    while i < len(ls) - 1:
        if ls[i] != ls[i+1] - 1:
            value = ls[i] + 1
            i = i + 1
        else:
            i = i + 1
    if value == 0 and ls[0] == 1:
        resultado = ls[len(l) - 1] + 1
    elif value == 0 and ls[0] != 1:
        resultado = 1
    else:
        resultado = value
    return print(resultado)