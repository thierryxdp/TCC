def maiores(lista_numero,n):
    """funçao que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, ordenados em ordem crescente
    list->list"""
    list.append(lista_numero,n)
    list.sort(lista_numero,reverse=True)
    a=list.index(lista_numero,n)
    b=lista_numero[:a]
    list.sort(b)#list.sort()不能atribui（ex:c=list.sort(b))
    
    return b

def acima_da_media(lista_notas):
    """função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média
    list->list"""
    
    tamanho=sum(lista_notas)
    media=int(tamanho/len(lista_notas))
    return maiores(lista_notas,media)