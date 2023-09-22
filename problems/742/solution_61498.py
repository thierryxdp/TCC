def substitui(s,x,i):
    '''função que retorna a própria string com o elemento da posição i trocado pelo caractere x:str,int,int->string'''
    return s[:i]+x+s[i+1:]