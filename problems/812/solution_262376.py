def retira_pontuacao(frase):
    """retorna a frase fornecida sem pontuação"""
    """str -> str"""
    return str.replace(frase, "!?_,.;:"," ")