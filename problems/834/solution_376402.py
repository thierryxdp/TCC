def media_matriz(matriz):
    """Retorna a meda de todos os numeros da matriz;
       Entrada: list;
       Saida: float;
   """
    soma = 0
    for numeros in matriz:
        soma += numeros
    media = soma/len(matriz)
    return media