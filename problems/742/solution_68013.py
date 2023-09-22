# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, exceto que o elemnto
       da posição i deve ser substituído pelo caractere x
       dados a string(s), um caractere(x) e um número
       inteiro(i) entre 0 e o comprimento da string.
       str,int,int -> str"""
    f=len(s)
    return s[0:i]+x+s[i+1:f]