def lingua_p(palavra):
    listaPalavra = []
    listaPalavra += palavra
    indice = 0
    tamanhoPalavra = len(palavra)
    while indice <= (len(palavra)+1):
        if listaPalavra[indice] in 'AEIOUaeiou':
            listaPalavra[indice+1:indice+1] = 'p'
        else:
            pass
        indice += 1
    return listaPalavra