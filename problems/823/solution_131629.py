def faltante(lista):
    """Descobre qual numero inteiro de um intervalo esta faltando, dado:
    uma lista com inteiros numerados de 1 a N(N-1), nao podendo ser 
    inteiros repetidos."""
    
    contador=1
    resultado=0
    
    while contador<=len(lista):

        if contador not in lista:
            resultado+=contador
        contador=lista[contador-1]+1
    if resultado==0:
        resultado+=len(lista)+1
    return resultado