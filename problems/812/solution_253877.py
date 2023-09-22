def retira_pontuacao(frase):
    """Recebe uma frase e retorna a mesma frase só que sem os caracteres de pontuação; str->str"""
    n = list(frase)
    return n[int(str.find(n, ','))]= ' '