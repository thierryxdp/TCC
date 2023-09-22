# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ substitu uma string x e a coloca con espeço correspondente ao número i em outra string s;
    string, string, int->string"""
    i=s[i]
    return s[:i]+ x + s[i:]