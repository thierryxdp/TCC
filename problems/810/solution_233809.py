def inverte(x):
    """ A função inverte a ordem das palavras da string de entrada. string-->string""" 
    a=str.replace(x,"."," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    h=str.split(g)
    i=h[::-1]
    return str.join(" ",i)