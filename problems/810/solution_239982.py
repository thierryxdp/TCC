def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
	x=frase.replace("!", " ")
    y=x.replace(".", " ")
    z=y.replace("?", " ")
    x1=z.replace("-", " ")
    y1=x1.replace(",", " ")
    z1=y1.replace(":", " ")
    x2=z1.replace(";", " ")
    
    
    a1=x2.lower()
    a2=a1.split(' ')
    w=list.reverse(a2)
    a3 = ' '.join(a2)

    return a3