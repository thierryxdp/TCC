def inverte(frase):
    if "." in (frase):
        frase = str.replace(frase,".","")
    if "!" in (frase):
        frase = str.replace(frase,"!","")
    if "?" in frase:
        frase = str.replace(frase, "?","")
    if "..." in (frase):
        frase = str.replace(frase,"...","")
    if "-" in (frase):
        frase = str.replace(frase,"-","")
    if "," in (frase):
        frase = str.replace(frase,",","")
    if ":" in (frase):
        frase = str.replace(frase,":","")
    if ";" in (frase):
        frase = str.replace(frase,";","")
    invertido = frase[::-1]
    return invertido