def acima_da_media(lista):
    """Função que fornece uma lista de números maiores que n"""
    n = int(sum(lista))/int(len(lista))
    list.append(lista,n)
    list.sort(lista)
    listafinal = lista[list.index(lista,n)+ 1:]
    varredura = 0
    listafinalissima = []
    while varredura <= len(listafinal):
        if listafinal[varredura] > n:
            varredura += 1 
            listafinalissima += [listafinal[varredura]]
        return listafinalissima