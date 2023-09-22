# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que define se um colchão passará por uma porta.
    list[int,int,int],int,int->bool"""
    medidas = [medidas[0], medidas[1], medidas[2]]
    if medidas[1] <= H:
        return True
    else:
        return False