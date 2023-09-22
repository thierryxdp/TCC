# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """parâmetros de entrada: duas listas de 3 elementos
    a função cria uma nova lista que intercala os elementos das listas de entrada
    assinatura: list, list -> list"""
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3