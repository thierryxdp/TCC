# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Fução que recebe duas listas com tamanho 3 de entrada e retorna uma nova lista
    com os elementos da lista1 e lista2. list,list->list"""
    lista1 = [lista1[0], lista1[1], lista1[2], lista1[3]]
    lista2 = [lista2[0], lista2[1], lista2[2], lista2[3]]
    lista_resultado = [lista1[0],lista2[0], lista1[1],lista2[1],lista1[2],lista2[2],lista1[3],lista2[3]]
    return lista_resultado