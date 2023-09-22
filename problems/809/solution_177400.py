# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que retorna a intercalação das listas L1 e L2, de tamanho 3, seguindo os parametros L1.0, L2.0, L1.1, L2.1, L1.2, L2.2
    list, list --> list"""
    conca1 = lista1 [0:1] + lista2 [0:1]
    conca2 = lista1 [1:2] + lista2 [1:2]
    conca3 = lista1 [2:] + lista2 [2:]
    return conca1 + conca2 + conca3