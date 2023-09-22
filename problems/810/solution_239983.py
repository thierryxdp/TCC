def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
	x=frase.replace("!", " ")
    y=x.replace(".", " ")
    z=x.replace("?", " ")
    x1=x.replace("-", " ")
    y1=x.replace(",", " ")
    z1=x.replace(":", " ")
    x2=x.replace(";", " ")
    
    
    a1=x2.lower()
    a2=a1.split(' ')
    w=list.reverse(a2)
    a3 = ' '.join(a2)

    return a3