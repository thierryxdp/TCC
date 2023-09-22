def substitui(s,x,i):
    '''recebe uma string, um caractere e 
    um número inteiro entre 0 e o comprimento da string
    e retorna a string S com o caractere X na posição 
    indicada por i
    string, int, int -> string'''
    
    return s[:i-1] + str(i) + s [i+1:]