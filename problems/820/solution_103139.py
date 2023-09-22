def posLetra(frase, letra, n):
    '''função que mostra a posição de uma letra em sua x repetição. str -> int'''
    i=0
    cont=0
    while i < len(frase):
    	if  frase[i] in letra:
            cont = cont + 1
        if cont  == n:
            return i
        else:
            return -1
    	i=i+1