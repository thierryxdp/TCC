# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, produtos)
	"""Recebe uma lista e um dict e retorna o valor total dos produtos da lista.
    	lista, dict -> float"""
    
    soma = 0
    
    for k, v in produtos.items:
        if k in lista:
            soma += v
    
    return soma