# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    Ph=H
    Pl=L
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if y>Ph:
        return True 
    else: 
        return False