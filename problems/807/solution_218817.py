def conta_frase(texto):
    '''Retorna o numero de frases presente em um texto dado
    	Entrada-> str
        Saida-> int'''
    texto1=texto.split('.')
    texto2=texto1.split('?')
    texto3=texto2.split('!')
    return len(texto3)