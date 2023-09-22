def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário onde cada palavra dessa
    string seja uma chave e tenha como valor o número de vezes que a 
    palavra aparece'''
    l=str.split(frases)
    x=0
    d={}
    while x < len(l):
        f=list.count(l, l[x])
        d[l[x]]=f
        x+=1
    return d