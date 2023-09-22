def freq_palavras(frases):
    'conta quantas vezes uma palavra aparece numa frase, string-->dict'
    dic=dict()
    palavras=frases.split()
    for i in palavras:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    return dic