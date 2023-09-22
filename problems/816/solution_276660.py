def maiores(lista_numero, n):
    
    nova_lista = insere(lista_numero,n)
    posicao = list.index(nova_lista,n)
    
    return nova_lista[posicao+1:]