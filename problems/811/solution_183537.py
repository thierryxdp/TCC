# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    altura=medidas[0]
    largura=medidas[1]
    comprimento=medidas[2]
    return (altura<h and comprimento<l) or (comprimento<h and altura<l) or (altura<h and largura<l) or (comprimento<h and largura<l)