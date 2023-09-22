def filtra_pares(tupla):
    contador=0
    tupla2=()
    while contador<len(tupla):
        if tupla[contador]%2==0:
            tupla2=tupla2+tupla[contador]
        contador=contador+1
    return tupla2