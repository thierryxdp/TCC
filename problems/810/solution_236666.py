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
    texto = texto[::-1]
    texto = str.join(" ",texto)
    texto = str.strip(texto)
    testo = str.replace(texto,"  "," ")
    return texto