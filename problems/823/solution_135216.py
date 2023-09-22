def faltante(lista):
    """Dada uma lista com N númeroes inteiros.Retorna O núnemro do elemento
que está faltando na lista N.lista(int)-->int."""
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+1
    i=0
    fta=0
    while i<lin(lista)-1:
        if lista[i+1] -lista[i]>1:
            fta= fta+lista[i]+1
        i=i+1
    return fta