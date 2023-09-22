def faltante(lista):
    n = len(lista) + 1
    ordenada=list.sort(lista)
    correta=list(range(1,n))
    i = 0             
    while i < len(lista):
        if ordenada[i] == correta[i]:
            i = i + 1
        if not ordenada[i] == correta[i]:
            return correta[i]