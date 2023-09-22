# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
   
    A= medidas[0]
    B= medidas[1]
  
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False