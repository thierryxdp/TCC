# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista correspondente as listas de entrada intercaladas
    	list, list -> list"""
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3