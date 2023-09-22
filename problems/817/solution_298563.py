def maiores (lista_inteiros,n):
    """função que dada uma lista de números inteiros
    'lista_inteiros' e um número inteiro 'n', retorna outra 
    lista, que contenha todos os números da lista original 
    maiores que n, ordenados em ordem crescente"""
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    indice_n= list.index(lista_inteiros,n)
    return lista_inteiros[indice_n+1:]

def acima_da_media (notas_alunos):
    """função que retorna uma lista ordenada com as notas
    que ficaram acima da média dados como entrada uma lista
    com as notas dos alunos de uma turma 'notas_alunos' """
    media = sum(notas_alunos)/len(notas_alunos)
    if media in notas_alunos:
        return (maiores(notas_alunos,media))[1:]
    else:
        return maiores(notas_alunos,media)