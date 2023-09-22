def freq_palavras(frases):
    '''define a frequencia de uma palavra ou seja quantas vezes ela se repete'''
    b=[]
    frases1=str.replace(frases,',','')
    frases2=str.replace(frases1,'.','')
    fraselista=str.split(frases2,' ')
    for i in fraselista:
        b.append(fraselista.count(i))
    l = []
    for i in b:
        l.append(i)
    c = []
    for i in fraselista:
        if i not in c:
            c.append(i)
              
    dicionario=(dict.fromkeys(c))
    for i in range (0,len(c)):
        dicionario[c[i]]=l[i]
    return dicionario