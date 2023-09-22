def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    frase2=frase.lower()
    x=frase2.replace("!", " ")
    y=x.replace(".", " ")
    z=y.replace("?", " ")
    x1=z.replace("-", " ")
    y1=x1.replace(",", " ")
    z1=y1.replace(":", " ")
    x2=z1.replace(";", " ")
    
    Y=x2.split(' ')
    w=list.reverse(Y)
    a3=" ".join(Y)

    return a3