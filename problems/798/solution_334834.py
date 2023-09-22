def freq_palavras(frases):
    frase="'"
    dic={}
    for l in frases: 
        if l== 'abcdefghijklmnopqrstuvwxyzáãâàõòóúíéêç': 
            frase+=l 
    for f in frase: 
        if f == dic:
            dic[f]=+1
        dic[f]=1
    return dic