def maiores(lista,n):
    '''dada uma lista de números inteiros e um inteiro n, retorna outra lista contendo todos os inteiros maiores que n da lista original;
    list, int --> list'''
    list.append(lista,n)
    list.sort(lista)
    quantas=list.count(lista,n)
    return lista[list.index(lista,n)+quantas:]

def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas dos alunos que ficaram acima da média;
    list, float --> list'''
    media=sum(lista)/len(lista)
    return maiores(lista,media)