# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, h, l):
    '''Define se um colchao paralelepipedo reto consegue passar em uma porta retangular
    recebe list, int, int e retorna: True/False'''
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    
    if ( h < l ):
        z = h
        h = l 
        l = z
    
    x = min(a, min(b, c))
    y = min(max(a, c), min(max(a,c), max(b,c)))
    
    if(x <= l and y <= h):
        return True
    else:
        return False