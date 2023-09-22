def media_matriz:
    """ Função que dada uma matriz de inteiros não vazia, retorna a média 
    de todos os números da matriz; lista -> float"""
    
    lista = []
    
    for i in matriz:
        for j in i:
            lista = lista + [j]
   
    return  round(sum(lista) / len(lista),2)