def media_matriz(matriz):
    """A função recebe como entrada uma matriz de inteiros
    não vazia, e deve retornar a média de todos os números
    da matriz com duas casas decimais de precisão
    Entrada: List
    Saída: Float"""
    
    lista=[]
    valor=0
    
    for i in list(range(len(matriz))):
        lista += matriz[i]
        valor= sum(lista)
    media= valor/len(lista)
    return round(media,2)