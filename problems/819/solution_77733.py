def filtraMultiplos(lis,num):
    """ Função que retorna todos os elementos contidos em 'l'
        list,int->list"""
    divisiveis = []
    elemento = 0
    while elemento < len(lis):
        if lis[elemento]%num == 0:
            divisiveis += (lis[elemento],)
            elemento += 1
            return divisiveis