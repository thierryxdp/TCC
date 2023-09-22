# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna os valores intercalados de duas listas em uma lista só,
    dado as duas listas contendo tres elementos.
    param lista1 -> list[int, int, int]
    param lista2 -> list[int, int, int]
    return -> list"""
    a, b, c = lista1
    d, f, g = lista2
    
    return [a, d, b, f, c, g]