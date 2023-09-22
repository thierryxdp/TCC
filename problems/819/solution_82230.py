def filtraMultiplos(lista,n):
    """"""
    var=0
    lista_=[]
    while var<len(lista):
        if lista[var]%n==0:
            var=var+1
    return lista_