def lingua_p(palavra):
    listaPalavra = []
    listaPalavra += palavra
    resposta = []
    vogais = 'aeiouáéíóúAEIOU'
    
    for i in range(len(listaPalavra)+len(listaPalavra)):
        qtdP = listaPalavra.count('p')
        if i > len(listaPalavra)-1:
            return ''.join(resposta)
        if listaPalavra[i] in vogais and listaPalavra[i] != listaPalavra[i-2]: 
            listaPalavra[i+1:i+1] = 'p'
            resposta = listaPalavra
        if listaPalavra[i] == 'p':
            listaPalavra[i+1:i+1] = listaPalavra[i-1]
            resposta = listaPalavra
    return ''.join(resposta)