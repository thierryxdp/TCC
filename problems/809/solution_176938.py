# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Calcula e retorna a intercalação das 2 listas"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[-1:1]+list2[-1:1]