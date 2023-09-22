def freq_palavras(f):
    '''Essa função ao receber uma string ela retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece'''
    ''' str ->dic'''
    p= str.split (f)
    f= {}
    for t in p:
        u = list.count(p,t)
        f[t]=u
        
    return f