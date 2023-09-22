def filtramultiplos(ln,n):
    """ Função que, dados uma lista e um número n,retorna outra 
    lista contendo todos os elementos da lista original que forem
    divisiveis por n
    list->list"""
    l1 = []
    contador = 0
    tamanho = len(ln)
    
    while contador < tamanho:
     
        if (ln[contador]% n)==0:
            l1 = l1 + [ln[contador]]
        contador = contador + 1

    return l1