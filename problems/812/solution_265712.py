def retira_pontuacao(x):
    """A função que dada uma frase, retorna uma frase com todos os caracteres 
    de pontuação foram substituidos por espaço.
    Assinatura: string -> string"""
    string = x
    caracteres = '?!,.'
    for x in range(len(characters)):
    string = string.replace(characters[x]," ")
    return x