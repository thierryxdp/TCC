def retira_pontuacao(frase):
    """substitui os caracteres de pontuacao por espacos;
    str -> str"""
    return str.replace(frase,'.',' ').replace(frase,',',' ').replace(frase,'-',' ').replace(frase,':',' ').replace(frase,';',' ').replace(frase,'!',' ').replace(frase,"?',' ')