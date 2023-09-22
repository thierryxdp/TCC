def retira_pontuacao(frase):
    """funcao que dada uma frase retira todos os caracteres de pontuacao str->str"""
    frase=str.replace(frase,"!", " ")
    frase=str.replace(frase,".", " ")
    frase=str.replace(frase,"?", " ")
    frase=str.replace(frase,"-", " ")
    frase=str.replace(frase,";", " ")
    frase=str.replace(frase,",", " ")
    return frase