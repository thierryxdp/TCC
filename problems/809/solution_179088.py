# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Tem como objetivo receber duas listas de tamanho 3
    e retornar uma lista de mesmo tamanha com seus elementos
    intercalados.
    lista > lista"""
    return [*sum(zip(lista1,lista2),())]