def retira_pontuacao(frase):
    """Funcao que dada uma frase, retorna a frase substituindo todos os carecteres de pontucao por espaco.
    str -> str"""

    if frase.count("-") != 0:
        frase = str.replace(frase, "-", " ")
    if frase.count(",") != 0:
        frase = str.replace(frase, ",", " ")
    if frase.count(":") != 0:
        frase = str.replace(frase, ":", " ")
    if frase.count(";") != 0:
        frase = str.replace(frase, ";", " ")
    if frase.count("!") != 0:
        frase = str.replace(frase, "!", " ")
    if frase.count("?") != 0:
        frase = str.replace(frase, "?", " ")
    if frase.count(".") != 0:
        frase = str.replace(frase, ".", " ")
    if frase.count("...") != 0:
        frase = str.replace(frase, "...", " ")
    
    return frase