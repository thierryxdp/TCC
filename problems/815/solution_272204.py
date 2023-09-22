def insere(lista_numero, n):
    '''funcao que dada uma lista de numeros inteiros crescentes e um numero inteiro n, retorna uma lista ordenada onde n fique na posicao correta;
       list, int-> list'''
    listafinal= list.insert(lista_numero, n)
    listafinal= list.sort(listafinal)
    return listafinal