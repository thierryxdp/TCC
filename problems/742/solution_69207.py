def substitui(s,x,i):
    '''função que recebe uma string(s),uma caractere(x) e um número inteiro(i) entre 0 e comprimento da string e retorna uma string igual a s, exceto que o elemento da posição (i) é substituido pelo caractere (x); string,string,int -> string'''
    return str(s[0:i-2]+x+s[i+2:])