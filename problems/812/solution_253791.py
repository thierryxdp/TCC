def retira_pontuacao(frase):
    """Recebe uma frase e retorna uma frase onde todos os caracteres de pontuação sejam substituidos por espaço; str -> str"""
    import re
    return re.sub("[,;&!?/.:]", frase, " ")