# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe um caractere x na posição i da string x e retorna uma concatenação de strings
    assinatura: string, int, int -> string
    testes:
    substitui ("pintalgar", "x", 2) == 'pixtalgar'
    substitui ("crestar", "1", 4) == 'cres1ar'
    """
    return s [ : i ] + x + s [i + 1 : ]