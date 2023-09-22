def media_matriz(matriz):
    """Essa função, dada uma matriz de inteiros não vazia,
	 retorna a média de todos os números da matriz com
	 precisão de duas casas decimais
     list -> float"""
    
    num = []
    
    for m in matriz:
        for n in m:
            list.append(num, n)
    media = sum(num)/len(num)
    
    return round(media, 2)