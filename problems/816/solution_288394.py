def maiores(lista, n):

    ''' lista int > int
    Dada uma lista, retorna outra lista, ordenada de forma crescente, apenas com os números maiores que n'''

    
    if n in lista:

        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]

        return listafinal

    if n not in lista:
    
        lista.append(n)
        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]

        return listafinal