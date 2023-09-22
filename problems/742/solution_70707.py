def substitui(s,x,i):
    '''retorna uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x
    str,str,int->str'''
    return x[0:i]+ s[0:i]+ s[i+1:len(s)]