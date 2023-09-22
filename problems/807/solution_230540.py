def conta_frase(text):
    '''Funcao que dado determinado texto, retornará a quantidade de frases. str ->int'''
    t=texto
    x=t.replace("..", "/")
    return x.count('.')+x.count('!')+x.count('?')