# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que retorna uma string s com o elemento da posição i substituído pelo caracter x
    string, int, int -> string """
    return s[0:i] + x + s[i+1:]