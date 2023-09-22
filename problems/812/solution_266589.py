def retira_pontuacao(frase):
    """Esta funcao recebe uma string e substitui sua pontuação por espaços
    str -> str"""
    while "." in frase:
        frase = frase.replace(".","  ")
    while "!" in frase:
        frase = frase.replace("!","  ")
    while "?" in frase:
        frase = frase.replace("?","  ")
    while "..." in frase:
        frase = frase.replace("...","  ")
    while "," in frase:
        frase = frase.replace(",","  ")
    while "  " in frase:
        frase = frase.replace("  ","")
    return frase