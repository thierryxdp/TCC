# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Pede duas listas de 3 elementos cada
    e retorna uma lista com 6 elementos, formada
    intercalando-se os elementos das duas primeiras listas.
    list, list->list"""
    lista3=[]
    for n in range(3):
        lista3=lista3+[lista1[n],lista2[n]]
    return lista3