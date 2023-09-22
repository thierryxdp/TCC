# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dado duas listas(lista1, lista2), gera uma 
	terceira lista com os números em ordem
    list, list -> list"""
    
    lista3 = lista1 + lista2
    
    return sorted(lista3)