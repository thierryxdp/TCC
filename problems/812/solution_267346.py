def retira_pontuacao(frase):
    """função que dada uma frase, retorna a frase com todos os caracteres  de pontuação  substituídos por espaço
    string -> string"""
    punc = '.,;:"'-'
    for elemento in frase:
        if elemento in punc:  
        frase = frase.replace(elemento, " ")
        return frase