# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    letras = list(s)
    letras[i] = x
    retorno = ""
    for i in letras:
        retorno += letras[i]