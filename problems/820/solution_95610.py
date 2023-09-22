def posLetra(string,letra,numero):
    '''funçao que dada uma string  uma letra e um numero 
    retorna qual a posiçao que o a letra aparece na string'''
    contador = 0
    if numero == 1:
        return string.find(letra)
    elif numero == 2:
        return string.find(letra,string.find(letra),len(string))
    else:
        return -1