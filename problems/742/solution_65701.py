def substitui(s,x,i):
    '''retorna uma string igual a s, porem, com o elemento da posição i trocado 
    pelo caractere da estrada x'''
    return str(s[0:i])+str(x)+str(s[i+1:])