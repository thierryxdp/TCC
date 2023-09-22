# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista obtida atraves da concatenacao dos elementos das listas de entrada;
    lista, list ->list"""
    lista1_intercalada=[lista1[0]]+[lista2[0]]+[lista1[1]]
    lista2_intercalada=[lista2[1]]+[lista1[2]]+[lista2[2]]
    return lista1_intercalada+lista2_intercalada