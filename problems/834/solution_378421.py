def media_matriz(matriz):
    '''Função que cálcula a média de todos os números da
    matriz de inteiros não vazia com exatamente duas casas
    decimais de precisão.
    list ->float'''
    ocorrencia=0
    total=0
    lista=[]
    for i in range(len(matriz)):        
        for j in range(len(matriz[i])):
            total=total+1
            list.append(lista,matriz[i][j])      
    return round(sum(lista)/len(lista),2)