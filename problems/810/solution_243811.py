def inverte(frase):
    """Função que inverte a frase completamente
    str -> str"""
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, ":"," ")
    frase = str.replace(frase, ";"," ")
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "!"," ")
    
    def frase