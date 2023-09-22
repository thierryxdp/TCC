def filtraMultiplos(lista,n):
    """dada uma lista e um numero n a funcao retorna uma lista com os numeros multiplos de n; list,int->list """
    var=0
    lista_=[]
    while var<len(lista):
        if lista[var]%n==0:
            list.append(lista_,lista[var])
        var=var+1
    return lista_