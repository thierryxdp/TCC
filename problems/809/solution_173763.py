# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que dados lista1 e lista2 de tamanho 3, gera uma lista3 que é formada intercalando os elementos de lista1 e lista2.
    lista, lista -> lista"""
    soma1 = lista1[0:1] + lista2[0:1]
    soma2 = lista1[1:2] + lista2[1:2]
    soma3 = lista1[2:] + lista2[2:]
    return soma1 + soma2 + soma3