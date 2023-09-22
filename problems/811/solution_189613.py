# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    areaColchao = 2*(medidas[1]*medidas[2]+medidas[1]*medidas[3]+
                     medidas[2]*medidas[3])
    areaPorta = L*H
    if areaColchao >= areaPorta:
        return True
    else:
        return False