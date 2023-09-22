def bolos (A: 'int', B: 'int', C: 'int') -> 'int':
'''A = número de xícaras de farinha de trigo
   B = número de ovos
   C = número de colheres de sopa de leite'''
return min ((A//2) + (B//3) + (C//5))