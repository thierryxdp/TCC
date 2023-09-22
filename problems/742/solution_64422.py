# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Substitui um elmento de s, na posicação i, por x
    string,string,int -> string """
    novastring = s[:i] + x + s[i+1:]
    return novastring