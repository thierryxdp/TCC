def substitui(s,x,i):
    '''retorna uma string igual a s, exceto que o elemento da posição i deve ser substiituído pelo caractere x'''
    return s[0:i]+'x'+s[i+1:]