def faltante(lista):
    for i in range(len(lista)):
       if i not in range(1, lista[-1]+1):
           i = faltante
    return faltante