# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string a s, com excecao do elemento da posicao 
    i que deve ser substituido pelo caractere x dados: s, x e i"""
    return s[:i]+x+s[i+1:]