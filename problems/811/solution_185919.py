# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    maiorcomprimento= min(medidas[1:3])
    maiorcomprimentoporta = max(H,L)
    if maiorcomprimento <= maiorcomprimentoporta:
        return True
    else:
        return False