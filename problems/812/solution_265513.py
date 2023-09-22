def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase com os caracteres de pontuação substituídos por espaço
    asssinatura: str -> str
    testes:
    retira_pontuacao() ==
    retira_pontuacao() ==
    retira_pontuacao() ==
    """
    travessao = str.replace (frase, "-", " ")
    virgula = str.replace (travessao, ",", " ")
    dois_pontos = str.replace (virgula, ":", " ")
    pvirg = str.replace (dois_pontos, ";", " ")
    retic = str.replace (pvirg, "...", " ")
    ponto = str.replace (retic, ".", " ")
    exc = str.replace (ponto, "!", " ")
    inter = str.replace (exc, "?", " ")
    return inter