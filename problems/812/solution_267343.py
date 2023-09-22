def retira_pontuacao(frase):
    """função que dada uma frase, retorna a frase com todos os caracteres  de pontuação  substituídos por espaço
    string -> string"""
    frase_pontuacao = frase
    punc = ".,;:-"
    for x in frase_pontuacao:
        if x in punc:  
        frase_pontuacao = frase_pontuacao.replace(x, " ")
        return frase_pontuacao