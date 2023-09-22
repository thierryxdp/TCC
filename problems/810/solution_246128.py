def retira_pontuacao(frase):
    """Função que retorna uma frase onde todos os seus caracteres de pontuação tenham sido substituídos por um espaço
    str -> str"""
    return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ")

def inverte(frase):
    """Função que retorna a mesma frase de entrada, porém com as palavras em ordem inversa, sem letras maiúsculas e sem pontuação
    str -> str"""
    return " ".join(str.split(str.lower(retira_pontuacao(frase)))[::-1])