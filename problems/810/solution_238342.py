def inverte(frase):
    """funcao que calcula e retorna uma outra frase de ordem inversa da original
    strin,strin-->string"""
    if "-":
        frase=str.replace(frase,"-"," ")
    if ",":
        frase=str.replace(frase,","," ")
    if ":":
        frase=str.replace(frase,":"," ")
    if ";":
        frase=str.replace(frase,":"," ")
    if "!":
        frase=str.replace(frase,"!"," ")
    if ".":
        frase=str.replace(frase,"."," ")
    if "?":
        frase=str.replace(frase,"?"," ")
    palavra =frase.split()   
    invertida=palavra.join(frase.split()[::-1])
    return invertida