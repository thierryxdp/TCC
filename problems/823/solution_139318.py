def faltante (lista):
    '''Função que irá retornar o número da peça que falta
    no quebra-cabeças
    lista -> int'''
    lista.sort()
    i = 0 
    while i < len(lista):
        if lista[i] != i+1:
            return i + 1
        i += 1
    return lista[-1] + 1