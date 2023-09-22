# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    """função que soma duas listas e retorna uma terceira lista com seu resultado"""
    res = l1+l2
    res[::2]= l1
    res[1::2]=l2
    return res