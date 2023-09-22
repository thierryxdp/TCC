# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
	lista = []
    A, B, C, = lista1
    D, E, F, = lista2
    lista += (A, D, B, E, C, F,)
    return lista