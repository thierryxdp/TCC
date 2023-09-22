def filtraMultiplos(lista, n):
    """dada uma lista e um numero como entrada, retorna os numeros da lista que sao divisiveis pelo numero dado, formando uma nova lista;
    list,int->list."""
    w=0
    aux=[]
    while w < len(lista) :
        if lista[w]%n==0:
            aux=aux+[lista[w]]
        w=w+1
    return aux