def retira_pontuacao(frase):
    """dada uma frase, retorna outra onde todos caracteres de pontuacao são substituidos por espaço"""
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
    return frase