def posLetra(string,letra,numero):
    """Dada uma string, uma letra e um número que indique a ocorrência desejada
    da letra (1 para  a primeira, 2 para a segunda...), a função retorna a
    posição da string que a letra está;"""
    i = 0
    indice = 0
    while i<len(string):
        if letra == string[i]:
            indice = indice + 1
            if indice == numero:
                indice2 = str.index(string,string[i],i)
        elif indice < numero:
            indice2 = -1
        i = i + 1
    return indice2