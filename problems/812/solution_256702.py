def retira_pontuacao(s):
    """Retira todos os caractereces de pontuação de uma frase e substitui por espaços"""
    return s.replace("!"," "), s.replace("-"," ")