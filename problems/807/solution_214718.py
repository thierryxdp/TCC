def conta_frases(texto):
    """dado um texto, essa funcao conta o numero de frase, 
    sendo a frase terminada por um ponto"""      
    a1= texto.count('.')
    b = texto.count('!')
    c = texto.count('?')
    d = texto.count('...')
    a = a1-(3*d)
    return (a+b+c+d)