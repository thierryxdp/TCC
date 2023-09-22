def substitui(s,x,i):
    '''funçao que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o 
    comprimento da string e retorna uma string igual a s, exceto o elemento da posiçao i, que deve ser 
    substituido pelo caractere x 
    str,int-->str,int'''
    return s[:i] + x + s[i+1:]