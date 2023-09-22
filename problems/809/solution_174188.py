# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
     if len(l1) != 3 or len(l2) != 3:
    
  l3 = []
  l3[0:0] = l1[0:1]
  l3[1:1] = l2[0:1]
  l3[2:2] = l1[1:2]
  l3[3:3] = l2[1:2]
  l3[4:4] = l1[2:3]
  l3[5:5] = l2[2:3]
  return l3