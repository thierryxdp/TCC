# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funcao que intercala listas"""
    listf = []
    for i in range(len(lista1)):
        listf.append(lista1[i])
        listf.append(lista2[i])
    return listf