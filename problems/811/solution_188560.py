# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ retorna true se o colchao passar pela porta,e false se nao passar, list,float,float->bool"""
    if H>=medidas[1]:
        return True
    elif H>=medidas[2]:
        return True
    elif L>=medidas[1]:
        return True
    elif L>=medidas[2]:
        return True
    else:
        return False