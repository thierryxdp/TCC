# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    colchao = medidas
    porta = h,l
    if colchao[1]>porta[0] and colchao[1]>porta[1]:
        return False
    else:
        return True