def inverte(frase):
    '''dada uma frase retorna  outra frase com as palavras da primeira frase de ordem invertida'''
    a=str.replace(frase,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,"."," ")
    d=str.replace(c,":"," ")
    e=str.replace(d,";"," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    h=str.lower(g)
    i=str.split(h)
    j=i[::-1]
    " ".join(j)