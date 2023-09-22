def media_matriz(matriz):
    '''dada uma matriz de inteiros não vazia, retorna a média de todos
    os números da matriz (com exatamente duas casas decimais de precisão
    list->float'''
    
    temp=0
    soma=0
    
    for i in matriz:
        temp=temp+len(i)
        soma=soma+sum(i)
   
	return round(soma/temp, 2)