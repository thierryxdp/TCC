def conta_frases(txt):
    """Recebe um texto e devolve o número de frases que contem nele atraves dos pontos finais, exclamações, interrogações e reticências;
    	str -> num"""
    mudanca=str.replace(txt,"...",".")
    frases1=str.split(txt,".")
    frases2=str.split(txt,"!")
    frases3=str.split(txt,"?")
    qtd=len(frases1)+len(frases2)+len(frases3)
    return qtd