def maiores(listainteiros, n):
    '''funcao que dada uma lista contendo apenas numeros inteiros e um numero inteiro n, retorna outra lista da original contendo apenas numeros maiores que n em ordem crescente;
       list, int->list'''
    list.insert(listainteiros, 0, n)
    list.sort(listainteiros)
    return listainteiros[list.index(listainteiros, n)+list.count(listainteiros,n):]

def acima_da_media(listanotas):
    '''funcao que dada uma lista com as notas dos alunos da turma, retorna uma nova lista ordenada com as notas que ficaram acima da média;
       list->list'''
    media= sum(listanotas)/len(listanotas)
    return maiores(listanotas,media)