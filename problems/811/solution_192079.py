# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, h, l):
    """Dada uma lista com as medidas do colchao, a altura e largura da porta, diz se o colchao passa pela porta ou nao
    list, int, int -> bool"""
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if l > b and h > a:
        return True
    else:
        return False