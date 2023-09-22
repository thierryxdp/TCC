def substitui(s,x,i):
    '''Esta funçãoo recebe uma string s, um caractere x
    e um numero inteiro i entre 0 e o comprimento da string,
    e retorna uma string igual a s, exceto que o elemento
    da posicao i deve ser substituido pelo caractere x
    string, int, int -> string'''
    
    nome = str(s)
    return nome[0:i] + x + nome[i+1:]