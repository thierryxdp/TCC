# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Função que recebe duas listas de mesmo tamanho e retorna uma lista com os elementos das duas intercalados.
	list -> list
    """
    lista3 = [0] * len(lista1) * 2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3