def lingua_p(palavra):
    '''Função que retorna a palavra dada traduzida para a lingua do p, isto é, ap´´os cada vogal da palavra dada, é inserida a sequència de letras'p' mais a vogal
    str->str'''
    novapalavra=''
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v''w','x','y','z']
    for x in range(len(palavra)):
        if palavra[x] in consoantes:
            novapalavra=novapalavra+palavra[x]
        else:
            novapalavra=novapalavra+palavra[x]+'p'+palavra[x]
    return novapalavra