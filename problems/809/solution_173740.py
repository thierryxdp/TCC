# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    l1 = [1,3,5]
    l2 = [2,4,6]
    l3 = l1[0:1] + l2[0:1] + l1[1:2] + l2[1:2] + l1[-1:] + l2[-1:]
    return l3