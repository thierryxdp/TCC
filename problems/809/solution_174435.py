# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas 2 listas com 3 elementos, intercala os elementos
       de ambas gerando uma nova lista
       
       Parameters:
       lista1: Primeira lista escolhida
       lista2: Segunda lista escolhida
       
       returns:
       Retorna uma nova lista, contendo os elemntos das duas listas de 
       entrada intercalados.
       list, list -> list"""
    lista3=lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]
    return lista3