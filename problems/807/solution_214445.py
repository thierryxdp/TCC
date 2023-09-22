def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    conta_texto = str.replace(texto,"...","#")
    return str.count(x,".")+ str.count(x,"!")+ str.count(x,"?")+ str.count(x,"#")