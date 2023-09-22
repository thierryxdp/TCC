def faltante(lista):
    n = len(lista) + 1
    correta=list(range(1,n+1))
    i = 0             
    while i < len(lista) and lista[i] == correta[i]:
            i = i + 1
    return correta[i]