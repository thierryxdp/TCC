def media_matriz (matriz):
    '''Retorna a soma de dus matrizes;list,list->list'''
    soma=0
    tamanho=0
    
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
        
    return soma / linha