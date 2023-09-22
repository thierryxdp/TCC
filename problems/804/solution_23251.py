def filtra_pares(numeros):
    '''Função que pega o termos pares de uma tupla(numeros) e retorna esses valores em outra tupla chamada \'tupla\''''
    tupla=()
    for c in numeros:
        if c%2==0:
        	tupla+=(c,)
    return tupla