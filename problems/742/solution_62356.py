def substitui(s,x,i):
    '''
    Função que retorna uma string igual a 's' com o elemento da posição i
    sendo substituido pelo caractere 'x',dada uma tupla (s,x,i)
    '''
    s[i]=x
    return s[0:i]+x+s[i+1:]