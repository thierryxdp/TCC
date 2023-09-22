def faltante(lista):
    faltando = []
    for i in range(1,len(lista)+2):
        if i not in lista:
            faltando.append(i)
    return faltando[0]