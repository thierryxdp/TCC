# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retornar uma terceira lista com elementos intercalados list --> list"""
    lista3 = []
    x = 0
    lista3 += [lista1[x],lista2[x]]
    x = 1
    lista3+= [lista1[x],lista2[x]]
    x = 2
    lista3 += [lista1[x],lista2[x]]
    return lista3