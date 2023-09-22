def retira_pontuacao(frase):
    """função que dada uma frase, retorna a frase com todos os caracteres  de pontuação  substituídos por espaço
    string -> string"""
    f = str(frase)
    pontuacao = str.punctuation
    for x in pontuacao:
        frase = frase.replace(x," ")
        return frase