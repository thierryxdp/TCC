def retira_pontuacao(txt):
    """
    Retira a pontuacao de uma frase (txt) e troca ela
    por espaco
    str -> str
    """
    delm = "{}"
    txt = txt.replace("...", delm)
    txt = txt.replace(".", delm)
    txt = txt.replace("!", delm)
    txt = txt.replace("?", delm)
    txt = txt.replace(";", delm)
    txt = txt.replace(":", delm)
    txt = txt.replace(",", delm)
    txt = txt.replace("-", delm)
    return txt.replace(delm, " ")