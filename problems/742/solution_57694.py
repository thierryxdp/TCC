# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''o caracter x vai ser plotado na string no lugar
    definidido por i(indice) em s'''

    fatia = s[:i]
    adiciona = x
    restoS = s[i+1:]

    return fatia+adiciona+restoS