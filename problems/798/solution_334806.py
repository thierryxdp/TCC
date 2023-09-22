def freq_palavras(frases): 
    frases=tuple(frases)
    dic={} 
    for proximo in frases:
        dic[proximo]=1 
        if proximo==dic[proximo]: 
            dic[proximo]=+1 
    return dic