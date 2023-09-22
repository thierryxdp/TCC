def retira_pontuacao(frase):
    """funçao que substitui todas as pontuaçoes por espaço
    str->str"""
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

def inverte(frase):
    """funçao que retorna outra frase com as mesmas palavras
    em ordem inversa e remove a pontuacao
    str->"""
    frase = retira_pontuacao(frase) 
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return (frase)