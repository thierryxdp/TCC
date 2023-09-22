def maiores(lista,n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n,
    lista --> lista"""
    
    if n not in lista:
        list.append(lista,n)
       
    list.sort(lista)
    indice = list.index(lista,n)
    
    fatiado = lista[indice + 1:]
    
    return fatiado
def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média,
    lista --> lista"""
    
    media = sum(lista)/ len(lista)
    
    return maiores(lista,media)