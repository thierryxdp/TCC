def lingua_p(palavra):
    listaPalavra = []
    listaPalavra += palavra
    resposta = []
    vogais = 'aeiouAEIOU'
    indice = 0
    while indice < len(listaPalavra):
        if listaPalavra[indice] in vogais:
            listaPalavra[indice+1:indice+1] = 'p'
            resposta += listaPalavra[0:indice+2]
        indice+=1
    return ''.join(listaPalavra)