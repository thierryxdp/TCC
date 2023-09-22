def conta_frase(texto):
    '''Retorna o numero de frases presente em um texto dado
    	Entrada-> str
        Saida-> int'''
    a=texto.split('.')
    b=texto.split('?')
    c=texto.split('...')
    d=texto.split('!')
    return len(a,b,c,d)