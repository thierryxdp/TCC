def lingua_p(palavra):
    """ Função que recebe uma palavra e retorna suas vogais acompanhadas
    pela letra "p",ou seja, a palavra é traduzida para língua do P
    str -> str"""
    palavra = palavra.lower()
    lista = list(palavra)
    for l in palavra:
        if l in 'aeiouáéíóú':
            m = lista.index(l)
            lista[m] = f'{l}p{l}'
    return ''.join(lista)