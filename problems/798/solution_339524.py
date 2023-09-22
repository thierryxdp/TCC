def freq_palavras(frases):
    part=frases.split()
    dic={}
    for tam in range(len(part)):
        if part[tam] in dic:
            dic[part[tam]]+=1
        else:
            dic[part[tam]]=1 
        
    return dic