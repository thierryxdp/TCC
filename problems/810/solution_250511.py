def retira_pontuacao(frase):
    travessao = str.replace (frase, "-", " ")
    virgula = str.replace (travessao, ",", " ")
    dois_pontos = str.replace (virgula, ":", " ")
    pvirg = str.replace (dois_pontos, ";", " ")
    retic = str.replace (pvirg, "...", " ")
    ponto = str.replace (retic, ".", " ")
    exc = str.replace (ponto, "!", " ")
    inter = str.replace (exc, "?", " ")
    return inter

def inverte(frase1):
    """Inverte a frase recebida na entrada retirando as pontuações
    assinatura: str -> str
    testes:
    inverte() ==
    inverte() ==
    """
    frase_limpa = retira_pontuacao(frase1)
    str.split(frase_limpa) = fpartes
    fpartes[::-1]