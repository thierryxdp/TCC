def inverte(frase):
    '''funcao que retorna a frase dada d forma invertida, sem letra maiuscula
    e sem pontuacao'''
    '.' != '...'
    a= str.replace(frase,'-',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,':',' ')
    d= str.replace(c,';',' ')
    e= str.replace(d,'?',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'.',' ')
    h= str.replace(g,'...',' ')
    k= h
    invercao = k
    f= str.split(invercao)
    return str.lower(str.join(' ',f[::-1]))