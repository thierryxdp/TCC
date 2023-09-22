def repetidos(numeros):
    '''Retorna quantas vezes um mesmo
       número foi repetido na lista;
       list->int'''
    contagem=list.count(numeros,numeros[:])
    return contagem