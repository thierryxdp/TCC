#
#
#
#
#
def maiores(lista_inteiros,n):
    list.sort(lista_inteiros)
    if n in lista_inteiros:
        list.index(lista_inteiros,n)
        i=list.index
        return lista_inteiros[i+1:]
    else:
        list.append(lista_inteiros,n)
        list.sort(lista_inteiros)
        list.index(lista_inteiros,n)
        i=list.index
        
        return lista_inteiros[i+1:]