# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui um item, daddo seu índice, numa dada string,
    por outro ítem assim dado'''
    lista = list(s)
    lista[i] = x
    return ''.join(lista)