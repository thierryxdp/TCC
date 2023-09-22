def retira_pontuacao(string):
    """retorna uma frase string de entrada
    sem os caracteres de pontuacao"""
    s=string.replace('.',' ')
    s=s.replace('!',' ')
    s=s.replace('?',' ')
    s=s.replace(',',' ')
    s=s.replace(';',' ')
    s=s.replace(':',' ')
    s=s.replace('-',' ')
    return s
def inverte(string):
    """retorna a frase da string de entrada com a ordem
    das palavras invertidas, sem pontuacao e sem letras
    maiusculas"""
    string=retira_pontuacao(string)
    string=string.lower()
    string=string.split(" ")
    return (string[-1:-5])