def maiores (lista_numerica, n):
    '''Função que nos retornará todos os números maiores que n
    em ordem crescente'''
    vazio = []
    list.sort(lista_numerica)
    # ordena os números da lista principal

    sucessor = n+1
    antecessor = n-1
    
    if n in lista_numerica:

        posição = lista_numerica.index(n)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posição:]
    
    elif antecessor in lista_numerica:
    
        posição_antecessor = lista_numerica.index(antecessor)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posição_antecessor:]
    
    elif sucessor in lista_numerica:
        
        posição_sucessor = lista_numerica.index(sucessor)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posição_sucessor:]
    
    else:
        return vazio