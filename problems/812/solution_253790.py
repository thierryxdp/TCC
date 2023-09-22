def retira_pontuacao(frase):
    """Recebe uma frase e retorna uma frase onde todos os caracteres de pontuação sejam substituidos por espaço; str -> str"""
    if '!' in frase:
        return replace(frase, '!', ' ')
    elif ',' and '.' in frase:
        return return replace(frase, ',', ' ') and return replace(frase, '.', ' ')