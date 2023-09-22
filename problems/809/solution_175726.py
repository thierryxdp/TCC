# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
    a função definida por intercala  que dadas duas listas
    lista1 e lista2 de tamanho n gera uma lista 3 que é formada
    pelos elementos intercalados de lista1 e lista2
    '''
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3