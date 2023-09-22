def posLetra(string,letra,numero):
    '''Retorna em que posição da string ocorre a ocorrência 
    indicada pelo número de entrada
    str,str,int->int'''
    i=0
    ocorrencias=str.count(string,letra)
    contador=0
    if ocorrencias<numero:
        return -1
    
    while contador<numero:
        if string[i]==letra:
            contador=contador+1
        i=i+1
    return i-1