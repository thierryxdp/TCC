def insere(lista_numero, n):
    '''Recebe uma lista de números inteiros em ordem crescente e um número
    inteiro "n", e inclui "n" na posição certa, de forma que a lista
    continue em ordem crescente.
    
    list, int -> list'''

    list.append(lista_numero, n)
    list.sort(lista_numero)

    return lista_numero


def maiores(listaInt, n):
    '''Recebe uma lista de números inteiros e um número inteiro "n" e retorna
    outra lista que contém os números da lista original maiores que "n".
    
    list -> list

    Explicação:
     Se o número "n" não estiver na lista original, ele é
    colocado nela (utilizando a função criada para o exercício anterior), antes
    de seguir o resto do desenvolvimento da função.
    
     A lista é ordenada(de forma crescente) e usando a função list.count()
    descobre quantas vezes o número "n" aparece na lista. Utilizando a função
    list.index() acha a posição da primeira ocorrêcia de "n" e, somando o
    número de "n" na lista e subtraindo 1, localiza a posição do último "n" da
    lista. A partir dessa posição encontrada faz um fatiamento da lista original
    apenas com os números maiores que o "n".'''

    if n not in listaInt:
        insere(listaInt, n)

    list.sort(listaInt)
    numero_de_n = list.count(listaInt, n)
    posicao_primeiro_n = list.index(listaInt, n)
    posicao_ultimo_n = posicao_primeiro_n +  numero_de_n -1
    maiores_n = listaInt[posicao_ultimo_n+1:]

    return maiores_n

def acima_da_media(notas):
    '''Recebe uma lista com as notas dos alunos de uma turma e retorna outra
    lista ordenada apenas com as notas acima da média.
    
    obs: utiliza as funções criadas para os dois exercícios anteriores
    
    list -> list'''

    somaNotas = sum(notas)
    numeroAlunos = len(notas)
    mediaTurma = somaNotas/numeroAlunos

    acimaMedia = maiores(notas, mediaTurma)

    return acimaMedia