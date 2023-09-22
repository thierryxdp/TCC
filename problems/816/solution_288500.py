def maiores(lista, n):
    '''função que retorna uma lista de ordem crescente,
    apenas com os números maiores que n. 
    assinatura: lista.int > int
    casos de teste: maiores([16, 12, 2, 4, 13, 18,], 20) ==[]
    maiores([16, 12, 2, 4, 13, 18,], 1) ==[2, 4, 12, 13, 16, 18]
    maiores([16, 12, 2, 4, 13, 18,], 13) ==[16, 18]'''
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