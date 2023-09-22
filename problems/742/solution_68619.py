# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string igual a "s" porém com a posição "i" da string
    trocada pelo caractere "x", dada a string s, o caractere x a ser trocado 
    e a posição i dele na string
    str, str, int -> str'''
    
    return s[0:i] + x + s[i+1:]