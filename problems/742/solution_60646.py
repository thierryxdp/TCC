# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que dada uma tring (s), um caracacter (x) e um numero inteiro (i)
    retorne uma string igual, porém o elemento da posição i será substituido pelo
    caracter x.
    str, int, int --> str"""
    original = s
    substitui = original.replace(i,x)
    return substitui