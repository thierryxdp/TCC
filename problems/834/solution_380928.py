def media_matriz(matriz):
    """Função que que dada uma matriz de inteiros 
    não vazia, retorna a média de todos os números 
    da matriz (com exatamente duas casas decimais 
    de precisão);
    list -> float"""
    

soma = 0    
tamanho = 0    
media = 0    

if matriz != []:
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            tamanho += 1
            soma += matriz[linha][coluna]
            media = soma / tamanho
            
return round(media, 2)