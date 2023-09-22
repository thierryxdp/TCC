def uppCons(frase):
    ''' Função que recebe uma frase e retorna a frase com todas
        as consoantes maiusculas, e os demais caracteres como
        estavam originalmente.
        : param frase: str
        : return: str 
    '''
    contador=0
    letra ='bcdfghjklmnpqrstvxwyzç'
    letra_maius=''
    while contador<len(frase):
        if frase[contador] in letra:
            letra_maius=letra_maius+frase[contador].upper()
        else:
            letra_maius=letra_maius+frase[contador]
        contador=contador+1
    return letra_maius