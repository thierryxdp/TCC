def retira_pontuacao(frase):
    """Dada uma frase, todos os sinais de pontuacao sejam substituidos por
       espacos"""
    y= '.' and ',' and ';' and ':' and '-'
    x= frase.replace(y,_,1)
    return x