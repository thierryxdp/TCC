def filtraMultiplos(lista, n):
    """dada uma lista e um numero, retorna uma lista com os multiplos desse numero;
    lista,int->lista"""
    w=0
    multiplos=[]
    while len(lista) :
        if lista[w]%n==0:
            mulltiplos = lista[w]+1
        w = w + 1
    return multiplos