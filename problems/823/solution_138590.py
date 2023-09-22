def faltante(lista):
    '''Recebe uma lista de numeros e retorna 
    o numero faltantes conforme a ordem 
    crescente
    
    list -> int
    '''
    list.sort(lista)
    
    lista_ordenada = list(range(1, len(lista)+2))
    
    contador = 0
    
    while len(lista_ordenada) > contador + 1:
        if lista[contador] != lista_ordenada[contador]:
            return lista_ordenada[contador]
        contador += 1 
    
    return lista_ordenada[-1]