# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''recebe medidas de um colchao e de uma porta, e retorna se o colchao passa pela porta ou nao
       list, float, float -> bool'''
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    
    if ((a and b)>(H and L) or ((a and c)>(H and L)) or ((b and c)>(H and L):
          return False
    elif (a and b and c)>(H and L):
          return False 
    else:
          return True