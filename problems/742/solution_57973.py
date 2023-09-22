# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "a função calcula a substituição do caractere na posição i da string por x string, int, int -> string"
    string1 = s[0:i]
    string2 = s[(i+1):]
    return string1+x+string2