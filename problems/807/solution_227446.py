def conta_frases(txt):
    """Recebe um texto e devolve o número de frases que contem nele atraves dos pontos finais, exclamações, interrogações e reticências;
    	str -> num"""
    mudanca=str.replace(txt,"...",".")
    frases1=str.split(txt,".")
    frases2=str.split(txt,"!")
    frases3=str.split(txt,"?")
    frasesfinal=list.append(frases1,frases2,frases3)
    qtd=len(frasesfinal)
    return qtd