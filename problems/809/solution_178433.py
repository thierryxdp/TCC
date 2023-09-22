# A função intercala os elementos da lista 1 e 2
# Parametros de entrada: lista 1 e 2, ambos são do tipo lista. Retorno tambem é uma lista.
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista3 = [lista1[0:1],lista2[0:1],lista1[1:2],lista2[1:2],lista1[2:3],lista2[2:3]]
    return lista3
    """Comentário: eu coloquei a lista3 do jeito que a questão pediu, mas por causa das [] entre os números do meu resultado
    o MT deu a questão como falhada"""