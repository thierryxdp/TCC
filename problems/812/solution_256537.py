def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase sem os caracteres de pontuação"""
    texto = str.replace(frase, '-',' ')
    texto = str.replace(texto, ',',' ')
    texto = str.replace(texto, ':',' ')
    texto = str.replace(texto, ';',' ')
    texto = str.replace(texto, '.',' ')
    texto = str.replace(texto, '!',' ')
    texto = str.replace(texto, '?',' ')
    return texto