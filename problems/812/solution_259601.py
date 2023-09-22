def retira_pontuacao(frase):
    """Funcao que retorna a frase onde todos os caracteres de pontuacao
    sao substituidos por espaços.
    str -> str"""
    pontuacao = "-,.:;?!"
    for p in pontuacao:
        frase = frase.replace(p, " ")
    return frase