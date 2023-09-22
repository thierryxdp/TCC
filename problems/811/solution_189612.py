# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    areaColchao = 2*(medidas[0]*medidas[1]+medidas[0]*medidas[2]+
                     medidas[1]*medidas[2])
    areaPorta = L*H
    if areaColchao >= areaPorta:
        return True
    else:
        return False