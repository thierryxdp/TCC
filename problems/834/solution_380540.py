def media_matriz(matriz):
    '''
    Função que dada uma matriz de inteiros não vazia, retorna a média de 
    todos os numeros da matriz, usando exatamente duas casas decimais de precisão
    list->float 
    '''
    soma=0
    for n in range(len(matriz)):
        
        M=matriz[n]
        for k in range(len(M)):
            soma=soma+M[k]
            
    media=(soma/(len(matriz)*len(matriz[0])))        
    return round(media,2)