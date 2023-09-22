def maiores(lista_numero,n):
    '''
    função que possui como entrada uma lista de números inteiros e um número 
    inteiro "n". Essa função irá retornar outra lista, que conterá todos os
    números da lista original maiores que "n", ordenados em ordem crescente.
    list,int->list

    '''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    x=lista_numero
    
    return [x for x in x if x>n]

def acima_da_media(lista_numero):
    '''
    função recebe como entrada uma lista com as notas dos alunos e retorna uma outra lista 
    com as notas que ficaram acima da média, em ordem crescente.
    '''
    k=sum(lista_numero)
    z=len(lista_numero)
    i=k/z
    
    return maiores(lista_numero,i)