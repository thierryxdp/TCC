def retira_pontuacao(s):
    """Retira todos os caractereces de pontuação de uma frase e substitui por espaços"""
    for pontos in "?-!.:;_,":
        s=s.replace(pontos," ")
    return s