def colisao(reta1,reta2):
    """
     Cada tupla nos dá uma reta, nós conseguimos construir um retângulo a partir
     disso, pois esses pontos tem de ser vértices diametralmente opostos
     para formar um retângulo. A entrada serão duas tuplas, cada uma
     representando uma reta, e essas retas representam os vértices diametralmente
     opostos de um retângulo, e cada uma das tuplas precisa ter entradas com
     valores inteiros. A saída será um valor booleano dizendo se há interseção
     desses retângulos determinados pelas retas.
     
     assinatura: tupla,tupla-----> boolean
     testes:
     colisao((0,0,1,1),(0,0,1,1))==True
     colisao((0,0,2,2),(1,1,3,3))==True
     colisao((0,0,1,1),(2,2,3,3))==False
     
     """
    
    x1,y1,x2,y2 = reta1
    x3,y3,x4,y4 = reta2

    if x2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    return True