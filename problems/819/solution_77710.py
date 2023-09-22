def filtraMultiplos(lista,numero):
    """ Função que retorna todos os elementos contidos em 'l'
        list,int->list"""
    divisiveis=[]
    elemento=0
    while elemento < len(lista):
        if lista[elemento]%n == 0:
            divisiveis += (l[elemento],)
            elemento += 1
            return divisiveis