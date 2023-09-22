def freq_palavras(frases):
    b=[]
    fraselista=str.split(frases,' ')
    for i in fraselista:
        b.append(fraselista.count(i))
    l = []
    for i in b:
        if i not in l:
            l.append(i)
    c = []
    for i in fraselista:
        if i not in c:
            c.append(i)
              
    dicionario=dict.fromkeys(c)
    for i in range (0,len(c)):
        dicionario[c[i]]=l[i]
    return dicionario