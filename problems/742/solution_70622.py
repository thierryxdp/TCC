def substitui(s,x,i):
    '''retorna uma string igual a s, 
    e o elemento da posição i será 
    substituído pelo caractere x.'''
    metade1= s[0:i]
    metade2= s[i+1:len(s)]
    return metade1 + x + metade2