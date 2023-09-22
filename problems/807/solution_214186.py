def conta_frases(texto):
    """Dado de entrada a string texto, retorna o número de frases nesse texto
    str==>int"""
    ponto = str.count(texto,".") - str.count(texto,"...")*3
    interrog = str.count(texto,"?")
    exclama = str.count(texto,"!")
    trespontos = str.count(texto,"...")
    
    return  ponto+interrog+exclama+trespontos