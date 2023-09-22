def retira_pontuacao(frase):
    """Retorna a frase de entreda em que todos os caracteres de pontuação são substituidos por espaço. string -> string"""
    return (frase.replace("!" and "?" and "..." and "-" and "," and ":" and ";" and "." , " "))