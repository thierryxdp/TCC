# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, h, l):
    """mostra se o colchão passa pela porta;
    list, int, int -> bool"""
    ac = medidas[0]
    cc = medidas[1]
    lc = medidas[2]
    if cc > h:
        if lc > l:
            return False
        else:
            return True
        elif lc < l:
            return True
        else:
            return True