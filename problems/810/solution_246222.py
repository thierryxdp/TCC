def inverte(frase):
    """ Função que recebe uma frase como parâmetro de entrada e 
    retorna uma outra frase que contenha as mesmas palavras da fra-
    se de entrada na ordem inversa, sem letras maiúsculas, e sem
    a pontuação.
    Entrada: str
    Saída: str
    """
    
    t = str(frase)
    
    t = str.replace(t, '-', ' ')
    t = str.replace(t, ',', ' ')
    t = str.replace(t, ':', ' ')
    t = str.replace(t, ';', ' ')
    t = str.replace(t, '.', ' ')
    t = str.replace(t, '-', ' ')
    t = str.replace(t, '?', ' ')
    t = str.replace(t, '!', ' ')
    
    t = str.lower(t)
    
    t = str.split(t," ")
    list.reverse(t)
    t1 = str.join(" ", t)
    
    
    return t