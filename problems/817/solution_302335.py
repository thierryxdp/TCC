def maiores (l_num,n):
    '''função em que dada uma lista de números inteiros  e um número inteiro (n)
    retorna outra lista, que contenha todos os números da lista original
    maiores que n ordenados em ordem crescente;
    list, int -> list'''
    if n in l_num: #para quando o número já estiver na lista
        list.sort(l_num)
        l1=list.index(l_num,n)
        return l_num[l1+1:]
    else: #para quando ele não estiver na lista
        list.append(l_num,n)
        list.sort(l_num)
        l1=list.index(l_num,n)
        return l_num[l1+1:]

def acima_da_media (lista):
    '''função em que dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acimada média;
    list -> list'''
    media=(sum(lista))/(len(lista))
    return maiores(lista,media)