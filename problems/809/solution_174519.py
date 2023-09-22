# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Intercala os elementos de duas listas diferentes,
    formando uma nova lista.
    list -> list"""
    return list.append(list.insert(list.insert(lista1,1,lista2[0]),2,lista2[1]),lista2[2])