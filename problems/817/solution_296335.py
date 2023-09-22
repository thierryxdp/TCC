def maiores(lista_numerica, n):
    '''
        recebe uma lista numerica e um numero inteiro retornando uma lista
        ordenad em ordem crescente, comosta pelos numeros maiore que o numero
        recebido
        entrada: lista, interiro
        saida: lista
    '''
    list.append(lista_numerica, n)
    list.sort(lista_numerica)
    list.reverse(lista_numerica)
    p=list.index(lista_numerica, n)
    lista_numerica=lista_numerica[0:p]
    list.reverse(lista_numerica)
    return lista_numerica


def acima_da_media(lista_notas):
    '''
        recebe uma lista com as notas dos alunos de uma turma e retorna uma
        lista ordenada, com as notas acima da media
        entrada: lista
        saida: lista
    '''
    md=sum(lista_notas)/len(lista_notas)
    lista_notas=maiores(lista_notas, md)
    return lista_notas