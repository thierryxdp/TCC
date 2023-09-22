# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Função que dada duas listas (lista1 e lista2) com 3 elementos, retorna
    uma lista formada pelo intercalado dos elementos da lista1 e lista2;
    list,list->list'''
    a, b, c = lista1
    d, e, f = lista2
    return [a,d,b,e,c,f]