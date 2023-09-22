def retira_pontuacao(x):
    """A função que dada uma frase, retorna uma frase com todos os caracteres 
    de pontuação foram substituidos por espaço.
    Assinatura: string -> string"""
    string = x
    caracteres = "?!,."
    string = ''.join( x for x in string if x not in characters)
    return x