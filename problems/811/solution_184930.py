# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def calchao(medidas,H,L):
    a=medidas[0]
    b=medidas[1]
  
    if(H<=a and L <=b) or (H<=b and L=a):
        return True