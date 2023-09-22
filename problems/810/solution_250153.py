def inverte(frase):
    '''
       Dada uma frase a função retorna a frase de trás para 
       frente, sem pontuação e sem letras maiúsculas
       str -> str
    '''
    str.lower(frase)
    lista = str.split(frase)
    list.reverse(lista)
    frase = str.join(' ',lista)
    return frase