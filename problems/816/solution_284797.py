def maiores(lista_inteiros,n):
    '''
     função que dada uma lista com números inteiros e um numero inteiro n, retorna outra lista
     que contenha todos os números da lista original maiores que n ordenados de forma crescente
     list---> list
    '''

    passo1=list.append(lista_inteiros,n)
    passo2=list.sort(lista_inteiros)
    posição= list.index(lista_inteiros,n)
    del(lista_inteiros[:posição+1])
            
        
    return lista_inteiros