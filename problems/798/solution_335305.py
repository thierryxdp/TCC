def freq_palavras(frases):
    frases=frases.split(' ')
    num=[0,1,2,3,4,5,6,7,8]
    for h in range(0,8):
        p=frases[h]
        c=frases.count(p)
    return{p:c}