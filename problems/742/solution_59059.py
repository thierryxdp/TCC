# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Substitui o carater da posicao dada pelo caracter dado"
    string_modificada= s[:i] + x + s[i+1]
    return string_modificada