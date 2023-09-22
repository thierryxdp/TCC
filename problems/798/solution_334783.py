def freq_palavras(frases): 
    dic={}
    i=0
    while i < len(frases): 
        if frases[i]==frases: 
            dic[frases[i]]=+1
        i=i+1
    return dic