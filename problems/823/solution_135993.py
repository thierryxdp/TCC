def faltante(lista):
    '''Função que retorna qual peça do quebra-cabeça está faltando
    list->int
    '''
    i=0
    a=1
    while i<len(lista):
        if lista[i]!= a:
            return a
        else:
            i+=1
            a+=1
    return lista[-1]+1