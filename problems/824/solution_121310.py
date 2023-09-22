def uppCons(frase):
    '''str-->str'''
    l='aeiouáéíóúâêãõ'
    x=0
    m=''
    while x<len(frase):
        if frase[x] not in l:
            m+= str.upper(frase[x])
        else:
            m+=frase[x]
        x+=1
    return m