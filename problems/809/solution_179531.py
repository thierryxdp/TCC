# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Essa função recebe listas lista1 e lista2 de tamanho 3 e
    retorna uma lista lista3 que intercala lista1 e lista2
    list, list-> list
    """
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]