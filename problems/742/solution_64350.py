def substitui(s,x,i):
    '''
    Função que recebe uma string s, um caractere x e um número 
    inteiro i entre 0 e o comprimento da string e retorna uma 
    string igual a s  exceto o elemneto da posição i que é 
    substituido pelo caractere x.
    
    string, int, int -> string
    '''
  
    return s[:i]+x+ s[:i:]