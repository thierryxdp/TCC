def media_matriz(matriz):
    """Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com duas casas decimais; lista->float"""
    
    soma = 0
    termos = len(matriz)*len(matriz[0])
    
    for lista in matriz:
        
        for n in lista:
            
            soma = soma + n
            
    return round(soma/termos,2)