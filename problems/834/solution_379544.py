def media_matriz(x):
    '''retorna a media de todos os numeros da matriz'''
    '''dic -> float'''
    
    soma = 0
    tamanho = 0
    
    for linha in x:
        soma +=sum (linha)
        tamanho += len(linha)
    return round (soma/tamanho, 2)