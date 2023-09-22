def inverte(texto):
    """
    	Funcao que dada uma frase, retorna a mesma, porém sem as 
        pontuacoes (".", "-", ",", ":" e ";").
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

    return h_lista