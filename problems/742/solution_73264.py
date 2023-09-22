# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que, dada uma str s, um caractere x e um 
    numero inteiro i entre 0 e len(s), retorna uma str s, 
    com o elemento da posicao i substituido pelo caractere x
    str,int,int -> str"""
    return s[:i] + x + s[i+1:]