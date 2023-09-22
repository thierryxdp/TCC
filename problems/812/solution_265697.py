def retira_pontuacao(x):
    """A função que dada uma frase, retorna uma frase com todos os caracteres 
    de pontuação foram substituidos por espaço.
    Assinatura: string -> string"""
    x = str.split(x,'!','.',',','?') 
    x = str.join(" ",x)
    return x