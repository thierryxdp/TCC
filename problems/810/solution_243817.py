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
    frase = str.lower(frase)
    lista = str.split(frase,' ')
    return str.join(' ',lista[::-1])