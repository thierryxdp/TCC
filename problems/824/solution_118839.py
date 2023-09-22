def uppCons(texto): 
    """ Função que recebe uma frase e retora a frase com
    as consoantes em maiúsculas.
    Entrada: string
    Saída: string"""
    indice=0
    frase='' 
    while indice<len(texto):
        if texto[indice] in 'bcdfghjklmnpqrstvxywzç':
            frase = frase + str.upper(texto[indice]) 
        else:
            frase = frase + texto[indice]
        indice=indice + 1
    return frase