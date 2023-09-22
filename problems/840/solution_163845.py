#importando o módulo math
import math

def bolos(A,B,C):
    '''calcula a quantidade de bolos que João consegue fazer dado a quantidade de ingrediente que ele tem em casa; int, int, int -> int'''
    return min(math.ceil(A/2),math.ceil(3/B),math.ceil(5/C))