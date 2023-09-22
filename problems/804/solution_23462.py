def filtra_pares(tupla):
    "função que recebe uma tupla com elementos inteiros e retorna uma nova tupla com os elementos pares da tupla anterior"
    lista1=[]
    for x in tupla:
        if x%2==0:
            lista1.append(x)
    tupla1=tuple(lista1[:])
    return tupla1