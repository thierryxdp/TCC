from math import*
def hashtag(s):
    """ Dado a string s, a função acrescenta uma # no início,
    no meio e no final da string.
    Parametros de Entrada: str;
    Retorna: str"""
    metade= len(s)
    auxiliar= metade%2
    
    if auxiliar == 0:
        auxiliar2 = metade//2
        return  '#'+s[:auxiliar2]+'#'+s[auxiliar2:]+'#'
    else:
        auxiliar3= ceil(metade/2)- 1
        return '#'+s[:auxiliar3]+'#'+s[auxiliar3:]+'#'