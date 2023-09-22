# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que retorna uma string igual a s, exceto o elemento da posição i que deve ser substituído pelo caractere x, parâmetros s, x e i
    string,string,int -> string"""
    return s[0:i]+x+s[1+i:]