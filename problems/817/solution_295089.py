def maiores(lista_inteiros,n):
    ''' Função que dada uma lista de números inteiros (lista_inteiros)
    e um número inteiro n, retorna outra lista que contenha todos os 
    números da lista passada que forem maiores que n
    Entrada: list,int
    Retorno: list '''

    insere_n = lista_inteiros + [n]
    list.sort(insere_n,reverse=True)
    maiores_n = insere_n[:list.index(insere_n,n)]
    list.sort(maiores_n)

    return maiores_n

# Exercício 5

def acima_da_media(lista_notas):
    ''' Função que dada uma lista com as notas dos alunos de uma turma
    (lista_notas), retorna uma lista ordenada com as notas que ficaram
    acima da média.
    Entrada: list
    Retorno: list '''

    media_notas = sum(lista_notas)/len(lista_notas)

    return maiores(lista_notas,media_notas)