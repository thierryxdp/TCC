def faltante(lista):
    n = len(lista) + 1
    correta=list(range(1,n+1))
    i = 0             
    while i < len(lista):
        if lista[i] == correta[i]:
            i = i + 1
        if not lista[i] == correta[i]:
            return correta[i]