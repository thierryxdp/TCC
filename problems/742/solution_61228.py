def substitui(s,x,i):
    '''Essa função recebe uma palavra(s), um caractere(x) e um número inteiro
    (i, sendo i entre 0 e o comprimento da string) e retorna a mesma palavra(s) 
    mas na posição (i) será substituído pelo caractere(x).
    str,str,int->str'''
    
    s1=s[:i]
    s2=[i+1:]
    i=str(i)
    
    return (s1+x+s2)