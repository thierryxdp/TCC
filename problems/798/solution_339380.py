palavras = []
    freq_palavras = []
    for x in range(len(listaTweets)):
            tweet = listaTweets[x]
            listaP = separa_palavras(tweet)
            for p in listaP:
                    if p in palavras:
                            indice = palavras.index(p)
                            freq_palavras[indice] += 1
                    else:
                            palavras.append(p)              
    return palavras, freq_palavras