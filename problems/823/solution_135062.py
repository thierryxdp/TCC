def faltante(lista):
    i = 1
    while i<=len(lista):
        if i not in lista and len(lista)<=i:
            return i
        i = i + 1