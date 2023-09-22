# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista com os elementos intercalados de lista1 e lista2
    lista, lista -> lista
    Explicação: cria uma nova lista com cada elemento dos argumentos organizados de forma intercalada"""
    ret = [
    	lista1[0],
        lista2[0],
        lista1[1],
        lista2[1],
        lista1[2],
        lista2[2]
    ]
    return ret