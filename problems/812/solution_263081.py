def retira_pontuacao(texto):
    """função que retorna a frase que todos os caracteres
    de pontuação sejam substituídos por espaço
    str -> str"""
    texto = texto.replace("-", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    return texto