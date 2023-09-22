def lingua_p(palavra):
    listaPalavra = []
    listaPalavra += palavra
    resposta = []
    vogais = 'aeiouAEIOU'
    indice = 0
    for i in range(len(listaPalavra)+(listaPalavra.count('p'))):
        if listaPalavra[i] in vogais and listaPalavra[i] != listaPalavra[i-2]:
            listaPalavra[i+1:i+1] = 'p'
            resposta = listaPalavra
        if listaPalavra[i] == 'p':
            listaPalavra[i+1:i+1] = listaPalavra[i-1]
            resposta = listaPalavra
    return ''.join(resposta)