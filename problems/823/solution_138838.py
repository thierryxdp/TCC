def faltante(lista):
    '''Essa função dada uma lista com N inteiros numerados de 1 a N, retona qual é o numero inteiro deste intervalo está faltando;
    Recebe lista com N numerados de 1 a n;
    Retorna o número inteiro deste intervalo está faltando.'''
    list.sort(lista)
    peca = 1
    pos = 0
    while peca == lista[pos]:
        peca = peca + 1
        pos = pos + 1
        if pos == len(lista):
            return peca
    return peca
#Essa função dada uma lista com N inteiros numerados de 1 a N, retona qual é o numero inteiro deste intervalo está faltando