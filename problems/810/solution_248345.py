def inverte(frase):
    
    a=frase.replace('...',' ',-1)
    b=a.replace('.',' ',-1)
    c=b.replace(',',' ',-1)
    d=c.replace(';',' ',-1)
    e=d.replace('?',' ',-1)
    f=e.replace('-',' ',-1)
    g=f.replace('!',' ',-1)
    h=g.replace(':',' ',-1)
    
    i=h.lower()
    lista_palavras=i.split(' ')
    lista_palavras_inversa=lista_palavras.reverse()
    frase_final=str.replace((' '.join(lista_palavras_inversa)),' ','')