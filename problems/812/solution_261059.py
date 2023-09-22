def retira_pontuacao(frase):
    """função que retorna uma frase sem nenhuma pontuação
    str -> str"""
    str.replace(frase,[-,:,;,.])
    return frase