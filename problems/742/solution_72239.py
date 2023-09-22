def substitui(s,x,i):
    ''' funcao que recebe uma string (s), um caractere (x) e um numero inteiro (i) entre 0 e o comprimento da string e retorna uma string igual a s exceto que o elemento da posicao i deve ser substuido pelo caractere x'''
     s[0:i:]+ str(x) + s[:i:]