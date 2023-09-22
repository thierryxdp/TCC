# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna uma lista formada pela intercalação dos elementos das listas 1 e 2, dadas a lista1 e a lista2"""
    lista=[]
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista