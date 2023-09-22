def maiores(lista_numeros,n):
    '''Função que, dada uma lista de números e um número n, retorna uma outra lista com somente os membros da primeira lista maiores que n.
    list, int --> list'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    return lista_numeros[(list.index(lista_numeros,n)+1):]

def acima_da_media(notas_alunos):
    '''Função que, dada uma lista com as notas dos alunos, retorna as notas acima da média em ordem crescente.
    list --> list'''
    ordenada = maiores(notas_alunos,(sum(notas_alunos)/len(notas_alunos)))
    ordenada2 = ordenada[:]
    del ordenada2[0]
    if sum(notas_alunos)/len(notas_alunos) in notas_alunos:
        return ordenada2
    else:
        return ordenada