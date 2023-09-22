# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
from math import sqrt
from math import sin
from math import cos
def colchao(medidas,H,L):
    """Dada as medidas do colchao e das portas, retorna se o colchao passa pela porta.
    list,int,int->bool"""
    hipotenusa = sqrt(H**2+L**2)
    l = sin(45)*medidas[2]
    h = sin(45)*medidads[2]
    if hipotenusa>medidas[2] and L>l and H>h:
        return 'True'
    else:
        return 'False'