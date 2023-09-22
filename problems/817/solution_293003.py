def maiores(lista, n):
    '''A função retornará uma lista com apenas os números maiores que (n).
    
    dados de entrada -> lista, int
    dados de saída -> lista'''
    
    list.append(lista,n) #inserindo o numero (n) no final da lista
    list.sort(lista) #colocando os números em ordem crescente
    posicao = list.index(lista,n) #descobrindo a posição do numero n na lista ordenada
    
    return lista[posicao+1:] #fatiamento da lista com os números maiores que n


def acima_da_media(lista):
    '''A função retornará as notas dos alunos que obtiveram grau superior a média
    da turma.'''
    Q = len(lista)
    Soma = sum(lista)
    Media = (Soma/Q) +1
    
    return maiores(lista,Media)