def uppCons(frase):
    ''' funcao que dada uma frase com consoantes e vogais,
    transforma todas as consoantes em maiusculo
    str -> str'''
    contador = 0 
    novafrase = ''
    while contador <len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novafrase+=frase[contador].upper()
        else:
                novafrase+=frase{contador].lower()
     contador = contador + 1
      return novafrase