def inverte(frase):
    
    if "—" in frase:
        frase= str.replace(frase,"—"," ")
    if "," in frase:
        frase= str.replace(frase,","," ")
    if ":" in frase:
        frase= str.replace(frase,":"," ")
    if ";" in frase:
        frase= str.replace(frase,";"," ")
    if "." in frase:
        frase= str.replace(frase,"."," ")
    if "-" in frase:
        frase= str.replace(frase,"-"," ")
    if "?" in frase:
        frase= str.replace(frase,"?"," ")
    if "!" in frase:
        frase= str.replace(frase,"!"," ")
    a=str.lower(frase)
    return a[::-1]