def retira_pontuacao(frase):
    """retira os caracteres da frase
    str ->str"""
    virgula = str.replace(frase,',','')
    travessao = str.replace(virgula,'-','')
    dois_pontos = str.replace(travessao,':','')
    pvirg = str.replace (dois_pontos, ";", "")
    retic = str.replace (pvirg, "...", "")
    ponto = str.replace (retic, ".", "")
    exc = str.replace (ponto, "!", "")
    inter = str.replace (exc, "?", "")
    return inter