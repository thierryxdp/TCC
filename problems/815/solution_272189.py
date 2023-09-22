def insere(lista_numero,n):
    '''funcao que, dada uma lista de numeros inteiros ordenada de forma crescente, insere
    o numero n de tal modo que a lista continue ordenada corretamente;
    list(int),int->list(int)'''
    nova_lista=lista_numero + [n]
    return list.sort(nova_lista)