def bolos (A: 'int', B: 'int', C: 'int') -> 'int':
# retorna o número maximo de bolos que jõao consegue fazer dado as quantidades de ingredientes    
    '''A = número de xícaras de farinha de trigo
       B = número de ovos
       c = número de colheres de sopa de leite'''
    return min ((A//2), (B//3), (C//5))