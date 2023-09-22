# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função deve receber uma string(s), um caractere (x) e um número inteiro(i),
    que esteja compreendido entre 0 e comprimento da string(s). Assim, a função 
    vai retornar uma string igual a s, com o elemento da posição do número i, substituído
    pelo caractere x.
    	O dado (s) e o dado (x) devem ser escritos entre aspas.
    str,str,int -> str"""
    s = str(s)
    x = str(x)
    i = int(i)
    return s[:i] + str(x) + s[(i+1):]