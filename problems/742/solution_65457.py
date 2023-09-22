def substitui(s,x,i):
    """funcao que dados de entrada uma string s, um caractere x 
    e um numero inteiro i entre 0 e o comprimento da string,
    retorna uma string igual a s, porem com o elemento da 
    posicao i substituido pelo caractere x;
    string, int, int -> string"""
    
    return s[0:(i)] + str(x) + s[(i+1):(len(s))]