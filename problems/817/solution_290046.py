def maiores(lista, n):
    """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maior que n
    	list, int -> list
    """
    nova_lista = lista[:]
    nova_lista = [ elem for elem in lista if elem >= n]
    nova_lista.sort()
    return nova_lista

def acima_da_media(notas):
    """ Função que dada uma lista de com as notas dos alunos, retorna uma lista ordenada com as notas que ficaram acima da média
    	list->list
    """
    sum = 0
    
    for nota in notas:
        sum+=nota
        
    media = sum / len(notas)
    acima_da_media = maiores(notas, media)
    
    return acima_da_media