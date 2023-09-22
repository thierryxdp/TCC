# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
from math import sqrt
from math import sin
from math import cos
def colchao(medidas,H,L):
    """Dada as medidas do colchao e das portas, retorna se o colchao passa pela porta.
    list,int,int->bool"""
    hipotenusa = sqrt(H**2+L**2)
    l1 = sin(45)*medidas[2]
    h1 = cos(45)*medidas[2]
    l2 = sin(45)*medidas[1]
    h2 = cos(45)*medidas[1]
    if hipotenusa>medidas[2] and L>l1 and H>h1:
        return 'True'
    elif hipotenusa>medidas[1] and L>l2 and H>h1:
        return 'True'
    else:
        return 'False'