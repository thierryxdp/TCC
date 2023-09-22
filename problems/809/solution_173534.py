# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
   	lista3 = list(range(6))
    lista3[::2] =lista1
    lista3[1::2] = lista2
    return lista3