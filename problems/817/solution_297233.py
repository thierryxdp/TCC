def insere(lista_numero,n):
    '''dada uma lista com numeros ordenados e um numero n, posiciona o numero n na posicao correta para a lista continuar ordenada;
    list->list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''dada uma lista com numeros ordenados e um numero n, posiciona o numero n na posicao correta para a lista continuar ordenada removendo os numeros menores que n;
    list->list'''
    insere(lista,n)
    a=list.index(lista,n)
    del lista[:a+1]
    return lista

def acima_da_media(lista):
    '''dada uma lista com as notas da turma, retorna as notas que ficaram acima da media da turma;
    list->list'''
    media=(sum(lista))/(len(lista))
    if media in lista:
        list.remove(lista,media)
    return maiores(lista,media)