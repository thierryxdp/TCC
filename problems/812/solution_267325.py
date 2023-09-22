def retira_pontuacao(frase):
    """função que dada uma frase, retorna a frase com todos os caracteres  de pontuação  substituídos por espaço
    string -> string"""
    for x in '.:;-,?!':
        frase = frase.replace(x,' ')
        return frase