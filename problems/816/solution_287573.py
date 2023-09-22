# questão 6
def maiores (lista_numerica, n):
    '''Função que nos retornará todos os números maiores que n
    em ordem crescente'''
    
    list.sort(lista_numerica)
    # ordena os números da lista principal

    if n in lista_numerica:

        posição = lista_numerica.index(n)
        # retorna a posição na lista em que o elemento estará
        
        return lista_numerica[posição:]