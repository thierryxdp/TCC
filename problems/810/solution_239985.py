def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
	x2=frase.replace("!", " ")
    
    a1=x2.lower()
    a2=a1.split('')
    w=list.reverse(a2)
    a3 = ' '.join(a2)

    return a3