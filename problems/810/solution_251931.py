def retira_pontuacao(frase):
    travessao = str.replace (frase, "-", " ")
    virgula = str.replace (travessao, ",", "")
    dois_pontos = str.replace (virgula, ":", "")
    pvirg = str.replace (dois_pontos, ";", "")
    retic = str.replace (pvirg, "...", "")
    ponto = str.replace (retic, ".", "")
    exc = str.replace (ponto, "!", "")
    inter = str.replace (exc, "?", "")
    return inter
def inverte(frase1):
    """Inverte a frase recebida na entrada retirando as pontuações
    assinatura: str -> str"""
    frase_limpa = retira_pontuacao(frase1)
    fpronta = str.lower(frase_limpa)
    fpartes = str.split(fpronta, " ")
    list.reverse(fpartes)
    resposta = str.join(" ", fpartes)
    return resposta