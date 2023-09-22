def retira_pontuacao(frase):
    """função que substitui a pontuação da frase de entrada(str) por espaço e retorna a frase alterada(str)"""
    return str.replace(frase,"-" and "," and ":" and ";" and "." and "?" and "!", " ")