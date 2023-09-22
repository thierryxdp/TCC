def conta_frases(texto):
    """ Dado um texto, retorna o numero de frases existentes, quando estas estao separadas por ponto final, exclamacao, interrogacao ou reticencias"""
    """entrada: str
    saida: int"""
    
    x = str.replace(texto,"...","#")
    
    return str.count(x,".")+ str.count(x,"!")+ str.count(x,"?")+ str.count(x,"#")