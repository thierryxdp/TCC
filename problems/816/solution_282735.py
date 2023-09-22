def maiores(lista_numeros, n):
    '''Função que insere um número n em uma dada lista e retorna apenas os
    números maiores que n em ordem crescente. Depois de  n adicionado e
    colocado em ordem na lista com as funções append() e sort(), é usada
    a função index() para descobrir o índice de n e atribuído esse inteiro
    à variável posicao. A função del retira da lista todos os elementos
    do índice 0 até n.
    list, int >> list
    '''
    
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    posicao = int(list.index(lista_numeros, n))
    del lista_numeros[:posicao + 1]
    return(lista_numeros)