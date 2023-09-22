def retirapontuacao(frase):
    if "." in frase:
        frase=frase.replace("."," ")
    if "!" in frase:
        frase=frase.replace("!"," ")
    if "?" in frase:
        frase=frase.replace("?"," ")
    if "..." in frase:
        frase=frase.replace("..."," ")
    if "," in frase:
        frase=frase.replace(","," ")
    if "_" in frase:
        frase=frase.replace("-"," ")
        return frase