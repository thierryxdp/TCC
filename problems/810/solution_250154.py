def inverte(frase):
    '''
       Dada uma frase a função retorna a frase de trás para 
       frente, sem pontuação e sem letras maiúsculas
       str -> str
    '''
    lista = str.split(str.lower(frase))
    list.reverse(lista)
    frase = str.join(' ',lista)
    return frase