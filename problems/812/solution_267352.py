def retira_pontuacao(texto):
    """função que dada uma frase, retorna essa frase com todos os caracteres de pontuação substituídos  por espaço l
    string -> string"""
    for x in '.:;-,?!':
        texto=texto.replace(x,' ')
    return texto