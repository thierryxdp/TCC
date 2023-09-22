def posLetra(frase, letra, n):
    '''função que mostra a posição de uma letra em sua x repetição. str -> int'''
    i=0
    j=0
    while i < len(frase):
        while j < n:
            if  frase[i]in letra:
                j=j+1
        i=i+1