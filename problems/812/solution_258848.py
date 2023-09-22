def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase onde todos os caracteres de
    pontuação sejam substituídos por espaço;
    string->string"""
    x=['-',',',':',';','.','!','?']
    y=str.split(frase,x)
    z=str.join(' ',y)
    return z