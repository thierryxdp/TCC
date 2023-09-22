def maiores(listaint,n):
    'dada uma lista de números inteiros e um número inteiro n retorne outra lista que contenha todos os números maiores que n.list,int-->list'
    list.append(listaint,n)
    list.sort(listaint)
    x= list.index(listaint,n)
    return listaint[x+1: ]

def acima_da_media(lista_nota):
    'dada uma lista com as notas dos alunos de uma turma retorne uma lista ordenads com as notas que ficaram acima da media. list,-->list'
    media= (sum(lista_nota))//(len(lista_nota))
    return maiores(lista_nota,media)