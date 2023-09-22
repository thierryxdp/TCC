# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef colchao(col, h, l):
  def colchao(medidas,H,L):
        '''Dada um lista com as dimensões do colcão, e
        list,float,float -> bool'''
        if medidas[1] <= H or medidas[1] <= 1:
            return True
        elif medidas[2] <= H or medidas[2] <= 1:
            return True
        else:
            return False