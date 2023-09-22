def retira_pontuacao(frase):
    """retira os caracteres da frase
    str ->str"""
    travessao = str.replace (frase, "-", " ")
    virgula = str.replace (travessao, ",", "")
    dois_pontos = str.replace (virgula, ":", "")
    pvirg = str.replace (dois_pontos, ";", "")
    retic = str.replace (pvirg, "...", "")
    ponto = str.replace (retic, ".", "")
    exc = str.replace (ponto, "!", "")
    inter = str.replace (exc, "?", "")
    return inter