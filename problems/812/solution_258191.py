def retira_pontuacao(frase):
    '''Entre com uma frase para ser retornada a mesma porem, sem pontuacao
    String -> String'''
    
    x=frase.replace("!", " ")
    y=x.replace(".", " ")
    z=y.replace("?", " ")
    x1=z.replace("-", " ")
    y1=x1.replace(",", " ")
    z1=y1.replace(":", " ")
    x2=z1.replace(";", " ")
    
    return x2