# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Dadas lista 1 e lista 2 com tamanho 3, gera uma lista 3 com os numeros das listas anteriores intercalados
    lista,lista->lista'''
    lista1='a','b','c'
    lista2='e','f','g'
    lista3=lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]
    return lista3