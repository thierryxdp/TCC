def colchao (dimensoes,h,l):
    '''função que, dadas as dimensões do colchão, avalie se ele passará ou não da porta. list -> bool.'''
         bc = dimensoes[0]
         hc = dimensoes[1]
         pc = dimensoes[2]

         if  bc <= h and hc <= l or bc <= h and pc <= l or hc <= h and bc <= l or hc <= h and pc <= l or pc <= h and bc <= l or pc <= h and hc <= l :
         
                  return 'True'
         else :
                  return 'False'