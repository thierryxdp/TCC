def media_matriz(matriz):
    '''função que dada uma matriz retorna a média de seus elemento com duas casas decimais de precisão
    entrada:list
    saida:float'''
    contador=0
    qtd=0
    for linha in matriz:
        for elementos in linha:
            	contador=contador+elementos
                qtd=qtd+1
    return round((contador/qtd),2)