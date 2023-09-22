def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    conta_texto = str.replace(texto,"...","@")
    return str.count(conta_texto,".")+ str.count(conta_texto,"!")+ str.count(conta_texto,"?")+ str.count(conta_texto,"@")