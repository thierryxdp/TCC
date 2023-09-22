def bolos(A,B,C):
    
    """A função irá retornar o número máximo de bolos que João poderá
    fazer, dados o número de xícaras de farinha de trigo A que ele tem
    em casa, o número B de ovos e o número C de colheres de sopa de leite
    que João possui
    int, int, int => int"""
    
    return min(A//2, B//3, C//5)