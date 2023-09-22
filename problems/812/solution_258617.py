def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a mesma ao invés de com caracteres de pontuação, sendo substituidos por espaço;
    str -> str"""
    return str.replace(frase,"!","?","."," ")