def uppCons(frase):
    '''str-->str'''
    l=
    x=0
    m=''
    while x<len(frase):
        if frase[x]!=l:
            m+= str.upper(frase[x])
        else:
            m+=frase[x]
        x+=1
    return m