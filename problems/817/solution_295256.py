def maiores(lista,n):
    '''Função que, dada uma lista qualquer e um número inteiro n, retorna uma lista com todos os números da lista original maiores que n.
list,int --> list'''
    lista_com_n = lista + [n]
    list.sort(lista_com_n)
    return lista_com_n[list.index(lista_com_n,n)+1:]

def acima_da_media(notas):
    '''Função que, dada uma lista com as notas dos alunos de uma turma, retorna uma nova lista ordenada somente com as notas acima da média
list --> list'''
    soma_das_notas = sum(notas)
    media_notas = soma_das_notas/len(notas)
    if media_notas in notas:
        notas_invertidas = sorted(notas,reverse=True)
        so_acima = notas_invertidas[0:list.index(notas_invertidas,media_notas)]
        return sorted(so_acima)
    else:
        return maiores(notas,media_notas)