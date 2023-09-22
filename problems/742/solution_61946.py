# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorn uma string igual a s, sendo s uma strin, x um caractere e i um número inteiro entre 0 e o comprimento da string.
       str, int, int -> str"""
    x[i]=x
    return s[0,i]+ x + s[i+1:]