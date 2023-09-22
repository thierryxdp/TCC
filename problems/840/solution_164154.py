def quantidade_bolo(a,b,c):
    """ Esta função retorna a quantidade máxima de bolos que João consegue fazer.
    
        Parameters:
            a: numero de xicaras de farinha de trigo disponiveis
            b: numero de ovos disponiveis
            c: numero de colheres de sopa de leite disponiveis
            
        Testes:
            quantidade_bolo(4,6,10) = 2
            quantidade_bolo(4,6,9) = 1
            
        Returns:
            Quantidade máxima de bolos que João consegue fazer
            float,int,float -> int.
    """
    farinha = a // 2
    ovos = b // 3
    leite = c // 5
    
    return min(farinha,ovos,leite)