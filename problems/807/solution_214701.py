def conta_frase(texto):
    """dado um texto, essa funcao conta o numero de frase, 
    sendo a frase terminada por um ponto"""      
    a = texto.count('.')
    b = texto.count('!')
    c = texto.count('?')
    d = texto.count('...')
    return int(a+b+c+d)