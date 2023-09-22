def conta_frase(texto):
    '''Retorna o numero de frases presente em um texto dado
    	Entrada-> str
        Saida-> int'''
    texto()
    texto1=texto.split('.')
    texto2=texto1.split('?')
    texto3=texto2.split('...')
    texto4=texto3.split('!')
    return len(texto4)