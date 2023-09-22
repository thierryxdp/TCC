def substitui(s,x,i):
    '''a funcao recebe uma string s, um caractere x e um n° inteiro i,
    retornauma string igual a s, com x no lugar do elemento i
    str, str, int -> str'''
    l=list(s)
    l[i]=x
    s=''.join(l)
    return (s)