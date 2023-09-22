def inverte(frase):
    '''
       Dada uma frase a função retorna a frase de trás para 
       frente, sem pontuação e sem letras maiúsculas
       str -> str
    '''
    lista = str.split(frase)
    list.reverse()
    frase = str.join(' ',frase)
    return frase