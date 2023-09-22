# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas com três elementos cada, a função forma uma
    terceira lista intercalando os elementos das duas primeiras.
    lista,lista-->lista
    
    Parâmetros
    lista1: lista que fornecerá os elementos 0,2 e 4 da nova lista
    lista2: lista que fornecerá os elementos 1,3 e 5 da nova lista"""
    return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]