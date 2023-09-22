def retira_pontuacao(texto):
    """Dada uma frase, retorna esta com os caracteres de pontuação substituídos por espaço
    asssinatura: str -> str
    testes:
    retira_pontuacao(O dia está lindo! O que quer fazer?) == O dia está lindo  O que quer fazer? 
    retira_pontuacao(Esse texto é complicado? Entendi...) == Esse texto é complicado  Entendi 
    retira_pontuacao(Que raiva! Esses momentos são  de fato  irritantes ) == Que raiva  Esses momentos são, de fato  irritantes 
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