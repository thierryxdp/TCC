# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    def intercala(lista1, lista2):
	''' funçao que, fornecidas duas listas (lista1 e lista2) 
    de tamanho padrao 3, retorna outra lista, formada pela
    intercalaçao dos elementos da primeira e da segunda listas
    list,list -> list'''
    soma1 = lista1 [0:1] + lista2 [0:1]
    soma2 = lista1 [1:2] + lista2 [1:2]
    soma3 = lista1 [2:] + lista2 [2:]
    return soma1 + soma2 + soma3