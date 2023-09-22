def retira_pontuacao(texto):
    """
    	Funcao que dada uma frase, retorna a mesma, porém sem as 
        pontuacoes (".", "-", ",", ":" e ";").
    """
    a= str.replace(texto,"."," ")
    b= str.replace(a,"-"," ")
    c= str.replace(b,","," ")
    d= str.replace(c,":"," ")
    e= str.replace(d,";"," ")
    f= str.replace(e,"?"," ")
    g= str.replace(f,"!"," ")
    return g