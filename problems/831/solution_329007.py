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
            list.append(novaPalavra, i)
            list.append(novaPalavra, 'p'+i)
        else:
            list.append(novaPalavra, i)
    return ''.join(novaPalavra)