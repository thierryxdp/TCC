def substitui(s,x,i):
    '''função que retorna uma string igual a "s", porem com o elemento, de 
    posicão dado pela entrada i, trocado pelo caractere dado como entrada em x'''
    if i>=0 and i<= len(s):
        return s.replace(s[i],x)