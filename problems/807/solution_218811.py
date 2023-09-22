def conta_frase(texto):
    '''Retorna o numero de frases presente em um texto dado
    	Entrada-> str
        Saida-> int'''
    a=texto.split('.')
    b=a.split('?')
    c=b.split('...')
    d=c.split('!')
    return len(d)