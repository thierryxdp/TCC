# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
from math import sqrt
def colchao(medidas,H,L):
    """Dada as medidas do colchao e das portas, retorna se o colchao passa pela porta.
    list,int,int->bool"""
    hipotenusa = sqrt(H**2+L**2)
    if hipotenusa>medidas[2]:
        return 'True'
    else:
        'False'