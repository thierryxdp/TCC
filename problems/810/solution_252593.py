def inverte(frase):
    if "." in (frase):
        frase = str.replace(frase,"."," ")
    if "!" in (frase):
        frase = str.replace(frase,"!"," ")
    if "?" in frase:
        frase = str.replace(frase, "?"," ")
    if "..." in (frase):
        frase = str.replace(frase,"..."," ")
    if "-" in (frase):
        frase = str.replace(frase,"-"," ")
    if "," in (frase):
        frase = str.replace(frase,","," ")
    if ":" in (frase):
        frase = str.replace(frase,":"," ")
    if ";" in (frase):
        frase = str.replace(frase,";"," ")
    invertido= frase.split()
    inverte = invertido[::-1]
    return ( ' '.join(inverte) )