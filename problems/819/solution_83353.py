def filtraMultiplos (lista,n):
    '''Esta função recebe uma lista de numeros e um numero, e retorna
    outa lista contendo todos os valores que forem divisíveis pelo
    número escolhido
    list, int >>> list '''
    
    multiplos = []
    contador = 0
    
    while contador < len (lista):
        if lista[contador] % n == 0:
            multiplos.insert (contador, lista[contador])
        contador = contador + 1
        
    return multiplos