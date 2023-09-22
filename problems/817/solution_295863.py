def maiores(lista,n):
    '''Dado uma lista de numeros inteiros e um numero inteiro n, retorna uma lista
contendo apenas numeros maiores do que n.list,int->list'''
    if n not in lista:
        list.append(lista,n)
    if n in lista:
        list.sort(lista)
        a=list.index(lista,n)
        lista2=lista[a+1:]
        return lista2      
def acima_da_media(lista2):
    '''Dado uma lista contendo notas de alunos de uma turma, calcula a media das notas e, utilizando-se
    da função maiores do exercicio anterior,retorna uma lista ordenada com as notas acima da media.list->list'''
    media=sum(lista2)/len(lista2)
    return(maiores(lista2,media))