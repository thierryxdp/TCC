def lingua_p(palavra):
    palavra = palavra.lower()
    lista = list(palavra)
    for letra in palavra:
        if letra in "aeiou":
            posicao = lista.index(letra)
            lista[posicao:posicao] = '{}p'.format(letra)
    return ''.join(lista)