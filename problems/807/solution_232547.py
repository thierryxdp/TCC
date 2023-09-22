def num_frases(frase):
    	frase = str.replace(frase," ", "")
    if "?" in frase:
        frase = str.replace(frase, "?"," ")
    if "!" in (frase):
        frase = str.replace(frase,"!"," ")
    if "..." in (frase):
        frase = str.replace(frase,"..."," ")
    if "." in (frase):
        frase = str.replace(frase,"."," ")
    return len(frase.split())