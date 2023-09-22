# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que retorna uma lista 'l3', que é uma lista intercalada 
    de duas outras recebidas como parâmetros"""
    l3 = []
    l3 = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return l3