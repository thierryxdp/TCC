def retira_pontuacao(frase):
    """funcao que dada uma frase retira todos os caracteres de pontuacao str->str"""
    frase=replace(frase,"!", " ")
    frase=replace(frase,".", " ")
    frase=replace(frase,"?", " ")
    frase=replace(frase,"-", " ")
    frase=replace(frase,";", " ")
    frase=replace(frase,",", " ")
    return frase