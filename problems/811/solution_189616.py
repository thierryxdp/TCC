# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    """função que recebe as medidas de um colchão e uma porta
e calcula se o colchão passa pela porta. int, int, int ->bool"""
    colchao = medidas
    porta = h,l
    if colchao[1]>porta[0] and colchao[1]>porta[1]:
        return False
    else:
        return True