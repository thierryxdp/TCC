# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    for i in range(2):
        for j in range(2):
            if medidas[i]<=H and medidas[j]<=L and i!=j:
                return True
            else :
                return False