# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    n1 = lista1[:1] # 1º da lista 1
    n2 = lista2[:1] #1º da lista 2
    n3 = lista1[1:2] #2º da lista 1
    n4 = lista2[1:2] #2º da lista 2
    n5 = lista1[2:] #3º da lista 1
    n6 = lista2[2:] #3º da lista2
    return n1 + n2 + n3 + n4 + n5