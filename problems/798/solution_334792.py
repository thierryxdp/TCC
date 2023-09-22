def freq_palavras(frases): 
    dic={} 
    for proxima in frases: 
        if proxima.count(frases): 
            dic[proxima]=1
    return dic