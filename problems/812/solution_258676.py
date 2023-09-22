def retira_pontuacao(frase):
    """Função que dada uma frase troque todos os caracteres de pontuação por espaços. string -> string"""
    return str.join(" ",str.split(frase))