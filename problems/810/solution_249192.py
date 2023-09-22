def inverte(texto):
    """ docs """
    
    texto_dividido = str.split(' ', texto_sem_pontuacao)
    texto_invertido = texto_dividido[::-1]
    
    return texto_invertido