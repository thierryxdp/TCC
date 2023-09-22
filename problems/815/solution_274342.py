def insere(list_numero,n):
    '''Funcao que dada a lista ordenada de numeros inteiros e um numero inteiro n, retorna uma lista com n incluido na posicao crescente
ent->list,int
saida->lista'''
    list_numero.append(n)
    list_numero.sort()
    return list_numero