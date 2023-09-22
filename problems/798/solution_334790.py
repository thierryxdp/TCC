def freq_palavras(frases): 
    dic={} 
    for proxima in frases: 
        if list.account(frases,proxima): 
            dic[proxima]=1
    return dic