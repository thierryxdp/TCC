def retira_pontuacao(frase):
    """Funcao que recebe uma frase como parametro, e retorna
    uma frase sem os sinais de pontuacao
    str->str"""
    return str.replace(frase,',',' ')