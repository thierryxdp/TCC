def maiores(lista_inteiros,n):
    ''' Dada uma lista com numeros inteiros e um numero n, a funcao retorna
    todos os numeros da lista original maiores que o numero n em outra lista;
    
    list, int -> list '''
    
    # 1. colocar o número n na lista original
    list.append(lista_inteiros,n)
    
    # 2. organizar (usar .sort) na ordem decrescente
    list.sort(lista_inteiros,reverse = True)
    
    # 3. descobrir o índice da primeira aparição de n
    indice_de_n = list.index(lista_inteiros,n)
    
    # 4. pegar todos os números do indice 0 até o anterior ao elemento n
    nova_lista = lista_inteiros[0:indice_de_n]
    
    # 5. arrumar essa lista com o sort em ordem crescente
    list.sort(nova_lista)
    
    return nova_lista