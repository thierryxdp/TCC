# Função que irá receber uma string s, um caractere x e um ńumero inteiro i entre 0 e o comprimento da string, e irá retornar uma string igual a s, exceto que o elementoda posiç̃ao i deve ser substitúıdo pelo caractere x.
# s, x, i
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[(i+1):]