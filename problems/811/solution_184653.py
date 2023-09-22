def colchao(medidas,H,L):
     '''Diz se um colchão retangular passará ou não pela porta em <medidas> deve se colocar as dimensões <A X B X C> do colchão'''

     if medidas[1] < H or medidas[2] < H or H == medidas[1] or H == medidas[2]:
          return True

     elif medidas[1] < L or medidas[2] < L or L == medidas[1] or L == medidas[2]:
          return True

     else:
          return False