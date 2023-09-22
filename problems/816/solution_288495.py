def maiores(lista, n):
    '''função que retorna uma lista de ordem crescente,
    apenas com os números maiores que n. 
    assinatura: lista.int > int
    casos de teste: '''
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