# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    ''' Função que, fornecidas duas listas (lista 1 e lista 2), de tamanho
    padrão 3, retorna outra lista, formada pela intercalação dos elementos das
    duas listas.
    list, list->list'''
    soma1 = lista1[0:1] + lista2[0:1]
    soma2 = lista1[1:2] + lista2[1:2]
    soma3 = lista1[2:] + lista2[2:]
    return soma1 + soma2 + soma3