def uppCons(f):
    ''' Função que resebe uma frase f e retorna a propria com suas consoantes em maiúsculo.
    str->str'''
    i=0
    j=list(f)
    s=len(j)
    while(i<s):
        if ( (j[i]!='a') and (j[i]!='e') and (j[i]!='i') and (j[i]!='o') and (j[i]!='u')):
            j[i]= str.upper(j[i])
    return str.join('',j)