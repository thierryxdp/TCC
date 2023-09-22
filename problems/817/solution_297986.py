def maiores(lista,n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna todos os números da lista original maiores do que n.
    list,int->list"""
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    x=list.index(lista,n)
    list.reverse(x)
    return lista[x+1:]
    
def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna as notas acima da média.
list->list"""
    media=(sum(lista))/len(lista)
    return maiores(lista,media)