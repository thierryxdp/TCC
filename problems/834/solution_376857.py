def media_matriz(matriz):
    """Funcao que retorna a media de todos os numeros da matriz com duas casa decimais;
    Entrada: list
    Saida: float"""
    n=0
    for linha in matriz:
        for aij in linha:
            soma+=aij            
            n+=1
    media=soma/n
    return media