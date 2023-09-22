def lingua_p(palavra):
    '''ao receber uma palavra, retorna a mesma palavra na
    lingua do P(onde após cada vogal, é inserida a letra
    p mais a própria vogal).
    str -> str'''
    palavra = palavra.lower()
    palavra = list(palavra)
    novaPalavra = []
    for i in palavra:
        if i in 'aáàâãeéêiíoóõôuú':
            indice = list.index(palavra, i)
            list.insert(novaPalavra, indice+1, 'p'+i)
    return ''.join(novaPalavra)