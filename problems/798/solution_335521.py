def feq_palavras(f):
    '''Essa função ao receber uma string ela retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece'''
    ''' str ->dic'''
    c=str.split(f)
    r={}
    for p in c:
        um = list.count(c,p)
        r[p]=um
        
    return r