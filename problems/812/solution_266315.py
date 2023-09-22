def	retira_pontuacao(f):
    """dada uma frase, retira todos os caracteres de pontuacao e troca por
    espacos. str->str"""
    return str.replace(f,str.punctuation,' ')