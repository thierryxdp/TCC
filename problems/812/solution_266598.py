def retira_pontuacao(frase):
    """Esta funcao recebe uma string e substitui sua pontuação por espaços
    str -> str"""
    if "." in frase:
        frase = frase.replace("."," ")
    if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    if "..." in frase:
        frase = frase.replace("..."," ")
    if "," in frase:
        frase = frase.replace(","," ")
 	if "-" in frase:
        frase = frase.replace("-"," ")
    return frase