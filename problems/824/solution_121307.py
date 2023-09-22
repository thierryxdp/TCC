def uppCons(frase):
    '''str-->str'''
    l=[a,e,i,o,u,á,é,í,ó,ú,â,ê,ã,õ]
    x=0
    m=''
    while x<len(frase):
        if frase[x]!=l:
            m+= str.upper(frase[x])
        else:
            m+=frase[x]
        x+=1
    return m