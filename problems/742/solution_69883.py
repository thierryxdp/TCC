def substitui(s,x,i):
    '''Função que dado um string(s), um caractere(x) e um inteiro(i) entre 0 e o comprimento da string, retorna uma string igual a s, exceto que o elemento da posição i é substituido pelo cara cterex;
       string, int, int -> string'''
    return s[:i]+x+s[i+1:]