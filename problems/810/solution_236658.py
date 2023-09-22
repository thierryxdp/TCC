def inverte(texto):
    """Inverte o texto trabalhado e tira pontuação"""
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,":"," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,"!"," ")
    texto = str.replace(texto,"?"," ")
    texto = str.lower(texto)
    texto = str.split(texto," ")
    return texto