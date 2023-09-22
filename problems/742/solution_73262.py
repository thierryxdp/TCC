# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que, dada uma string s, um caractere x 
    e um numero inteiro i entre 0 e len(s), retorna
    uma string s, com o elemento da posicao i substituido
    pelo caractere x
    str,int,int -> str"""
    s[i] == x
    return s[:i] + s[i+1:]