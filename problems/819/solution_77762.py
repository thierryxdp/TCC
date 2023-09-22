def filtraMultiplos(lista,numero):
    """ Função que retorna todos os elementos contidos em 'l' 
         list,int->list"""
    divisiveis = []
    elemento = 0
    while elemento < len(l):
        if lista[elemento]%numero == 0:
            divisiveis += (lista[elemento],)
            elemento += 1
            return divisiveis