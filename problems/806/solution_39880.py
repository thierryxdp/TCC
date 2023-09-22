def colisao(r1x1: float, r1y1: float, r1x2: float, r1y2: float,
    r2x1: float, r2y1: float, r2x2: float, r2y2: float) -> bool:
    """Verifica se há colisão entre os retângulos representados pelas
       coordenadas

       Parameters:
       r1x1: Coordenada x do primeiro ponto do retângulo 1
       r1y1: Coordenada y do primeiro ponto do retângulo 1
       r1x2: Coordenada x do segundo ponto do retângulo 1
       r1y2: Coordenada y do segundo ponto do retângulo 1
       r2x1: Coordenada x do primeiro ponto do retângulo 2
       r2y1: Coordenada y do primeiro ponto do retângulo 2
       r2x2: Coordenada x do segundo ponto do retângulo 2
       r2y2: Coordenada y do segundo ponto do retângulo 2

       Returns:
       Se há colisão (sobreposição) entre os retângulos 1 e 2 no plano 2D

       Examples:
       colisao(0, 0, 1, 1, 0, 0, 1, 1) == True
       colisao(0, 0, 2, 2, 1, 1, 3, 3) == True
       colisao(0, 0, 1, 1, 2, 2, 3, 3) == False
    """
    return ((r2x1 > r1x2 and r2y1 > r1y2)
           or (r1x1 > r2x2 and r1y1 > r2y2)) == False