def inverte(texto):
    """
    	Funcao que dada uma frase inverte a ordem das palavras e deixa todas
    	as letras em minusculas
    """
    a= str.lower(texto)

    b= str.replace(a,"."," ")
    c= str.replace(b,"-"," ")
    d= str.replace(c,","," ")
    e= str.replace(d,":"," ")
    f= str.replace(e,";"," ")
    g= str.replace(f,"?"," ")
    h= str.replace(g,"!"," ")

    h_lista = h.split()
    
    list.reverse(h_lista)

    h_invertida = " ".join(h_lista)

    return h_invertida
    

    
    list.reverse(h_lista)

    return h_lista