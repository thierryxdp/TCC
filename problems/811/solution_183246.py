def colchao (dimensoes,h,l):
    '''funcao que vai dizer se o colchao passara ou nao da porta. float,float,float,float,float -> bool.'''
         bc = dimensoes[0]
         hc = dimensoes[1]
         pc = dimensoes[2]

         if  bc <= h and hc <= l or bc <= h and pc <= l or hc <= h and bc <= l or hc <= h and pc <= l or pc <= h and bc <= l or pc <= h and hc <= l :
         
                  return 'True'
         else :
                  return 'False'