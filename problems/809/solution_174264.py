# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que dadas duas listas 'lista1' e 'lista2' de tamanho 3, gera uma lista3 que e formada intercalando elementos das listas 'lista1' e 'lista2'"""
    lista3 = []
    for a,b in zip(lista1, lista2):
        lista3.append(a)
        lista3.append(b)
    return lista3