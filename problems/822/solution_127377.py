def repetidos(lista):
    '''Recebe como entrada uma lista de números
    e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    list -> int'''
    x = 0
    rep = []
    while x < len(lista):
        numero_ocorrencias_de_cada_numero = (lista.count(lista[x]))
        rep += [numero_ocorrencias_de_cada_numero]
        return(max(rep))
        x += 1