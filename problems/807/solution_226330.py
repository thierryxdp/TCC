def conta_frases(frase):
    """dado uma string(frase) retorna o numero de palavras"""
    """str->int"""
    return(2*(str.count(frase,'.'))-(str.count(frase,'...'))+2*(str.count(frase,'...'))+2*(str.count(frase,'!'))+2*(str.count(frase,'?')))