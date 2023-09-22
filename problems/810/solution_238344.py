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
    palavra=frase.split()   
    invertida=srt.join(palavra[::-1] for palavra in frase.split())
    return invertida