# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    lista = [s]
    if len(lista) < i:
        lista[i] += x
        return lista
    else len(lista) > i:
        return lista