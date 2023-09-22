def posLetra(string,letra,numero):
    ''' essa funçao retorna em qual posição da string aquela letra está'''
    if str.count(string,letra) < numero:
        return -1
    else:
        lista = []
        i = 0
        while i<len(string):
            list.append(lista,string[i])
            i= i + 1
        b=0
        while b<(numero - 1 ):
            posicao = list.index(lista,letra)
            lisa[posicao] = ''
            b = b + 1
        return list.index(lista,letra)