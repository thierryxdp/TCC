def faltante(l):
    i = 0
    value = 0
    while i < len(l) - 1:
        if l[i] != l[i+1] - 1:
            value = l[i] + 1
            i = i + 1
        else:
            i = i + 1
    if value == 0:
        resultado = l[len(l) - 1] + 1
    else:
        resultado = value
    return print(resultado)