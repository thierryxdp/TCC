def maiores(l,n):
    ''' retorna outra lista que contenha todos os números de l, dada uma lista de números inteiros e um número inteiro n;
    list,int -> list '''
    if n in l:
        list.sort(l)
        l1 = list.index (l,n)
        return l[l1+1:]
    else:
        list.append(l,n) 
        list.sort(l)
        l1 = list.index(l,n)
        return l[l1+1:]

def acima_da_media(l):
    ''' retorna uma lista ordenada com as notas que ficaram acima da média, dada uma lista l com as notas dos alunos de uma turma;
    list -> list '''
    media=sum(l)/len(l)
    return maiores(l,media)