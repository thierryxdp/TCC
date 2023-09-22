# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    passa = False
    for i in range(3):
        for j in range(3):
            if medidas[i]<=H and medidas[j]<=L and i!=j:
                passa = True
    return passa