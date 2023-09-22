def conta_frases(txt):
    """Recebe um texto e devolve o número de frases que contem nele atraves dos pontos finais, exclamações, interrogações e reticências;
    	str -> num"""
    mudanca=str.replace(txt,"...",".")
    mudanca2=str.replace(txt,'!','.')
    mudanca3=str.replace(txt,'?','.')
    frases=str.split(txt,'.')
    return frases