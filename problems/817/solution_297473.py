def maiores(lista,n):
    '''retorna uma lista com todos os numeros da lista de numeros
    inteiros original que são maiores que um numero n;
    list,int->list'''
    list.append(lista,n)
    list.sort(lista)
    pos=list.index(lista,n)
    return lista[pos+1:]

def acima_da_media(notas):
    '''retorna uma lista com todas as notas contidas na lista notas que estão
    acima da média entre as notas dos alunos da turma;
    list->list'''
    media=sum(notas)/len(notas)
    if media in notas:
        list.append(notas,n)
        list.sort(notas)
        pos=list.index(notas,n)
        return notas[pos+2:]
    else:
        return maiores(notas,media)