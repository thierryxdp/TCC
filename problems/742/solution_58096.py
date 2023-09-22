'''Dados pelo usuário uma string s, um caractere x e um número inteiro i entre
0 e o comprimento s, o programa retorna uma string semelhante à s, porém, com 
o caractere da posição i substituícdo pelo caractere x'''

# string, int, int -> string
def substitui(s,x,i):
    comprimento = len(s)
    edicao1 = s[0:i]
    f = comprimento-i
    edicao2 = s[i+1:comprimento]
    return edicao1 + x + edicao2