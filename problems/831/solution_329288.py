def lingua_p(palavra):
    """"""
    palavra = palavra.lower()
    lista = list(palavra)
    for l in palavra:
        if l in 'aeiouáéíóú':
            m = lista.index(l)
            lista[m] = f'{l}p{l}'
    return ''.join(lista)