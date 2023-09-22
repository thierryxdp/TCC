def conta_frases(texto):
    """
    Função que dado um texto armazenado em uma string, conta o número de frases
    que aparecem neste texto.
    str -> int
    """
    a=str.replace(texto,"...","#")
    b=str.replace(a,".","#")
    c=str.replace(b,"!","#")
    d=str.replace(c,"?","#")
    frases=str.split(d,"#")
    return len(frases)-1