# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função de substituição entre string s, caractere x e um numero inteiro i entre 0 e o comprimento da string """
 s=list(s)
s[i] = x
return "".join(s)