def contafrases(frase):
    """Esta funcao recebe uma string e conta o numero de frases nesta
    str -> int"""
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    frasecomreticencias = (reticencias*3)
    if "..." in frase:
        return (ponto+interrogacao+exclamacao+reticencias-frasecomreticencias)
    else:
        return (ponto+interrogacao+exclamacao)


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

# questão 4
def inverte(frase):
    """Essa função recebe uma frase, remove sua pontação e a inverte
    str -> str"""
    frase = retira_pontuacao(frase)
    frase = frase.lower
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)