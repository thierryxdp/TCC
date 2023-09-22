# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    
    if a<=L and b<=H:
        return True
    else:
        return False