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

def inverte(frase):
    """Funcao que dada uma frase retorna a mesma com suas palavras invertidas, sem letras maiusculas e sem pontuacao.
    str -> str"""
    
    frase = retira_pontuacao(frase)
    lista = str.split(frase)
    inverso = lista[::-1]
    inversoFrase = str.join(" ", inverso)
    return str.lower(inversoFrase)