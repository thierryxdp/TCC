def retira_pontuacao(frase):
    """função que dada uma frase, retorna a frase com todos os caracteres  de pontuação  substituídos por espaço
    string -> string"""
    frase_pontuacao = frase
    punc = ".,;:-"
    for ele in frase_pontuacao:
        if ele in punc:  
        frase_pontuacao = frase_pontuacao.replace(ele, " ")
        return frase_pontuacao