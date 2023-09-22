def inverte(frase):
    '''função que dade uma frase retorne uma outra frase que 
    contenha as mesmas palavras da frase de entrada na ordem 
    inversa,sem letras maiúsculas, e sem ppontuação;
    string->string'''
    s=frase
    a=str.replace(s,'.',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,'-',' ')
    e=str.replace(d,';',' ')
    f=str.replace(e,'...',' ')
    g=str.replace(f,'!',' ')
    h=str.replace(g,'?',' ')
    x=str.lower(h)