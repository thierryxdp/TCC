def maiores(numeros,n):
    '''Função que dada uma lista de números inteiros, retorna outra 
    lista somente com os números maiores que o parâmetro N dado na função'''
    
    return numeros[numeros.index(n)+numeros.count(n):]