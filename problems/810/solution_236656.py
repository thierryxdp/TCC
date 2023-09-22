def inverte(texto):
    """Inverte o texto trabalhado e tira pontuação"""
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,":"," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,"!"," ")
    texto = str.replace(texto,"?"," ")
    return str.lower(texto)[::-1]