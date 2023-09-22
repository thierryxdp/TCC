# questão 6
def maiores (lista_numerica, n):
    '''Função que nos retornará todos os números maiores que n
    em ordem crescente'''
    vazio = []
    list.sort(lista_numerica)
    # ordena os números da lista principal

    sucessor = n+1
    
    if n in lista_numerica:

        posicao = lista_numerica.index(n)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posicao:]
    
    elif sucessor in lista_numerica:
        
        posicao_sucessor = lista_numerica.index(sucessor)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posicao_sucessor:]
    
    elif lista_numerica[0]>n:
        return lista_numerica
    
    else:
        return vazio