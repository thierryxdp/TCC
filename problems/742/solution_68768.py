def substitui(s,x,i):
    '''funcao que retorna uma string atraves da colocacao
       do numero inteiro i e o caractere x na string s
       str, str, int -> str'''
    return s[0:i] + x + s[i+1:]