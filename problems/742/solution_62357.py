def substitui(s,x,i):
    '''
    Função que retorna uma string igual a 's' com o elemento da posição i
    sendo substituido pelo caractere 'x',dada uma tupla (s,x,i)
    '''
    if i==0:
        s=str(x)+s[i:]
    else:
        return s=[0:i]+str(x)+s[i+1:]